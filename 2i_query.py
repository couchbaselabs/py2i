#!/usr/bin/env python
import socket
import struct
import proto.query_pb2 as P

class ResponseDone(Exception): pass
FL_PROTOBUF = 0x10


class QueryHandler(object):
    def __init__(self, host, bucket, name):
        self._host = host
        self._bucket = bucket
        self._name = name
        self._sock = None

    def connect(self):
        hstr, pstr = self._host.split(':')
        pstr = int(pstr)
        self._sock = socket.create_connection((hstr,pstr))

    def _pack_msg(self, msg):
        header = struct.pack("!IH", len(msg), FL_PROTOBUF)
        return header + msg

    def write_request(self):
        pl = P.QueryPayload()
        pl.version = 1

        req = pl.scanAllRequest
        req.indexName = self._name
        req.bucket = self._bucket
        req.pageSize = 10
        req.limit = 0

        buf = pl.SerializeToString()
        buf = self._pack_msg(buf)
        self._sock.sendall(buf)

    def _handle_message(self, msg):
        if msg.HasField('stream'):
            for r in msg.stream.indexEntries:
                print "Entry: PK={0}. K={1}".format(r.primaryKey, r.entryKey)
            if msg.stream.HasField('err'):
                print "Found stream error: {0}".format(msg.stream.err.error)
        elif msg.HasField('streamEnd'):
            raise ResponseDone()
        else:
            print msg.ListFields()
            raise ValueError("Unknown stream!" + str(msg))

    def do_read(self):
        buf = bytearray()
        while True:
            while len(buf) < 6:
                oldlen = len(buf)
                buf += self._sock.recv(4096)
                newlen = len(buf)
                if oldlen == newlen:
                    raise Exception('Connection closed!')

            rlen, rflags = struct.unpack("!IH", bytes(buf[:6]))
            if rflags != FL_PROTOBUF:
                raise ValueError("Unexpected flags: {0:X}".format(rflags))

            cur_buf = buf[6:]
            while len(cur_buf) < rlen:
                cur_buf += self._sock.recv(4096)

            buf = cur_buf[rlen:]
            cur_buf = cur_buf[:rlen]

            msg = P.QueryPayload()
            msg.ParseFromString(str(cur_buf))
            try:
                self._handle_message(msg)
            except ResponseDone:
                break

if __name__ == "__main__":
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('-H', '--host', help="Query port", default="localhost:7000")
    ap.add_argument('-b', '--bucket', help="Bucket", default="default")
    ap.add_argument('-n', '--name', help="Name of index to query", required=True)
    options = ap.parse_args()
    qh = QueryHandler(options.host, options.bucket, options.name)
    qh.connect()
    qh.write_request()
    qh.do_read()
