# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='query.proto',
  package='q2i',
  serialized_pb='\n\x0bquery.proto\x12\x03q2i\"\x16\n\x05\x45rror\x12\r\n\x05\x65rror\x18\x01 \x02(\t\"\xa1\x03\n\x0cQueryPayload\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\x31\n\x11statisticsRequest\x18\x02 \x01(\x0b\x32\x16.q2i.StatisticsRequest\x12+\n\nstatistics\x18\x03 \x01(\x0b\x32\x17.q2i.StatisticsResponse\x12%\n\x0bscanRequest\x18\x04 \x01(\x0b\x32\x10.q2i.ScanRequest\x12+\n\x0escanAllRequest\x18\x05 \x01(\x0b\x32\x13.q2i.ScanAllRequest\x12#\n\x06stream\x18\x06 \x01(\x0b\x32\x13.q2i.ResponseStream\x12\'\n\x0c\x63ountRequest\x18\x07 \x01(\x0b\x32\x11.q2i.CountRequest\x12)\n\rcountResponse\x18\x08 \x01(\x0b\x32\x12.q2i.CountResponse\x12(\n\tendStream\x18\t \x01(\x0b\x32\x15.q2i.EndStreamRequest\x12)\n\tstreamEnd\x18\n \x01(\x0b\x32\x16.q2i.StreamEndResponse\"O\n\x11StatisticsRequest\x12\x17\n\x04span\x18\x01 \x02(\x0b\x32\t.q2i.Span\x12\x11\n\tindexName\x18\x03 \x02(\t\x12\x0e\n\x06\x62ucket\x18\x04 \x02(\t\"R\n\x12StatisticsResponse\x12#\n\x05stats\x18\x01 \x02(\x0b\x32\x14.q2i.IndexStatistics\x12\x17\n\x03\x65rr\x18\x02 \x01(\x0b\x32\n.q2i.Error\"|\n\x0bScanRequest\x12\x17\n\x04span\x18\x01 \x02(\x0b\x32\t.q2i.Span\x12\x10\n\x08\x64istinct\x18\x02 \x02(\x08\x12\r\n\x05limit\x18\x03 \x02(\x03\x12\x10\n\x08pageSize\x18\x04 \x02(\x03\x12\x11\n\tindexName\x18\x05 \x02(\t\x12\x0e\n\x06\x62ucket\x18\x06 \x02(\t\"T\n\x0eScanAllRequest\x12\x10\n\x08pageSize\x18\x01 \x02(\x03\x12\r\n\x05limit\x18\x02 \x02(\x03\x12\x11\n\tindexName\x18\x03 \x02(\t\x12\x0e\n\x06\x62ucket\x18\x04 \x02(\t\"\x12\n\x10\x45ndStreamRequest\"P\n\x0eResponseStream\x12%\n\x0cindexEntries\x18\x01 \x03(\x0b\x32\x0f.q2i.IndexEntry\x12\x17\n\x03\x65rr\x18\x02 \x01(\x0b\x32\n.q2i.Error\",\n\x11StreamEndResponse\x12\x17\n\x03\x65rr\x18\x01 \x01(\x0b\x32\n.q2i.Error\"1\n\x0c\x43ountRequest\x12\x11\n\tindexName\x18\x01 \x02(\t\x12\x0e\n\x06\x62ucket\x18\x02 \x02(\t\"7\n\rCountResponse\x12\r\n\x05\x63ount\x18\x01 \x02(\x03\x12\x17\n\x03\x65rr\x18\x02 \x01(\x0b\x32\n.q2i.Error\"0\n\x04Span\x12\x19\n\x05range\x18\x01 \x01(\x0b\x32\n.q2i.Range\x12\r\n\x05\x65qual\x18\x02 \x03(\x0c\"5\n\x05Range\x12\x0b\n\x03low\x18\x01 \x02(\x0c\x12\x0c\n\x04high\x18\x02 \x02(\x0c\x12\x11\n\tinclusion\x18\x03 \x02(\r\"2\n\nIndexEntry\x12\x10\n\x08\x65ntryKey\x18\x01 \x02(\x0c\x12\x12\n\nprimaryKey\x18\x02 \x02(\x0c\"]\n\x0fIndexStatistics\x12\x11\n\tkeysCount\x18\x01 \x02(\x04\x12\x17\n\x0funiqueKeysCount\x18\x02 \x02(\x04\x12\x0e\n\x06keyMin\x18\x03 \x02(\x0c\x12\x0e\n\x06keyMax\x18\x04 \x02(\x0c')




_ERROR = descriptor.Descriptor(
  name='Error',
  full_name='q2i.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='error', full_name='q2i.Error.error', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=42,
)


_QUERYPAYLOAD = descriptor.Descriptor(
  name='QueryPayload',
  full_name='q2i.QueryPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='q2i.QueryPayload.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='statisticsRequest', full_name='q2i.QueryPayload.statisticsRequest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='statistics', full_name='q2i.QueryPayload.statistics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scanRequest', full_name='q2i.QueryPayload.scanRequest', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scanAllRequest', full_name='q2i.QueryPayload.scanAllRequest', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stream', full_name='q2i.QueryPayload.stream', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='countRequest', full_name='q2i.QueryPayload.countRequest', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='countResponse', full_name='q2i.QueryPayload.countResponse', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='endStream', full_name='q2i.QueryPayload.endStream', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='streamEnd', full_name='q2i.QueryPayload.streamEnd', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=462,
)


_STATISTICSREQUEST = descriptor.Descriptor(
  name='StatisticsRequest',
  full_name='q2i.StatisticsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='span', full_name='q2i.StatisticsRequest.span', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='indexName', full_name='q2i.StatisticsRequest.indexName', index=1,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bucket', full_name='q2i.StatisticsRequest.bucket', index=2,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=464,
  serialized_end=543,
)


_STATISTICSRESPONSE = descriptor.Descriptor(
  name='StatisticsResponse',
  full_name='q2i.StatisticsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stats', full_name='q2i.StatisticsResponse.stats', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='err', full_name='q2i.StatisticsResponse.err', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=545,
  serialized_end=627,
)


_SCANREQUEST = descriptor.Descriptor(
  name='ScanRequest',
  full_name='q2i.ScanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='span', full_name='q2i.ScanRequest.span', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='distinct', full_name='q2i.ScanRequest.distinct', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='limit', full_name='q2i.ScanRequest.limit', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pageSize', full_name='q2i.ScanRequest.pageSize', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='indexName', full_name='q2i.ScanRequest.indexName', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bucket', full_name='q2i.ScanRequest.bucket', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=629,
  serialized_end=753,
)


_SCANALLREQUEST = descriptor.Descriptor(
  name='ScanAllRequest',
  full_name='q2i.ScanAllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pageSize', full_name='q2i.ScanAllRequest.pageSize', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='limit', full_name='q2i.ScanAllRequest.limit', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='indexName', full_name='q2i.ScanAllRequest.indexName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bucket', full_name='q2i.ScanAllRequest.bucket', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=755,
  serialized_end=839,
)


_ENDSTREAMREQUEST = descriptor.Descriptor(
  name='EndStreamRequest',
  full_name='q2i.EndStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=841,
  serialized_end=859,
)


_RESPONSESTREAM = descriptor.Descriptor(
  name='ResponseStream',
  full_name='q2i.ResponseStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='indexEntries', full_name='q2i.ResponseStream.indexEntries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='err', full_name='q2i.ResponseStream.err', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=861,
  serialized_end=941,
)


_STREAMENDRESPONSE = descriptor.Descriptor(
  name='StreamEndResponse',
  full_name='q2i.StreamEndResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='err', full_name='q2i.StreamEndResponse.err', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=943,
  serialized_end=987,
)


_COUNTREQUEST = descriptor.Descriptor(
  name='CountRequest',
  full_name='q2i.CountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='indexName', full_name='q2i.CountRequest.indexName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bucket', full_name='q2i.CountRequest.bucket', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=989,
  serialized_end=1038,
)


_COUNTRESPONSE = descriptor.Descriptor(
  name='CountResponse',
  full_name='q2i.CountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count', full_name='q2i.CountResponse.count', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='err', full_name='q2i.CountResponse.err', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1040,
  serialized_end=1095,
)


_SPAN = descriptor.Descriptor(
  name='Span',
  full_name='q2i.Span',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='range', full_name='q2i.Span.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='equal', full_name='q2i.Span.equal', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1097,
  serialized_end=1145,
)


_RANGE = descriptor.Descriptor(
  name='Range',
  full_name='q2i.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='low', full_name='q2i.Range.low', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='high', full_name='q2i.Range.high', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='inclusion', full_name='q2i.Range.inclusion', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1147,
  serialized_end=1200,
)


_INDEXENTRY = descriptor.Descriptor(
  name='IndexEntry',
  full_name='q2i.IndexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entryKey', full_name='q2i.IndexEntry.entryKey', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='primaryKey', full_name='q2i.IndexEntry.primaryKey', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1202,
  serialized_end=1252,
)


_INDEXSTATISTICS = descriptor.Descriptor(
  name='IndexStatistics',
  full_name='q2i.IndexStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='keysCount', full_name='q2i.IndexStatistics.keysCount', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='uniqueKeysCount', full_name='q2i.IndexStatistics.uniqueKeysCount', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keyMin', full_name='q2i.IndexStatistics.keyMin', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keyMax', full_name='q2i.IndexStatistics.keyMax', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1254,
  serialized_end=1347,
)

_QUERYPAYLOAD.fields_by_name['statisticsRequest'].message_type = _STATISTICSREQUEST
_QUERYPAYLOAD.fields_by_name['statistics'].message_type = _STATISTICSRESPONSE
_QUERYPAYLOAD.fields_by_name['scanRequest'].message_type = _SCANREQUEST
_QUERYPAYLOAD.fields_by_name['scanAllRequest'].message_type = _SCANALLREQUEST
_QUERYPAYLOAD.fields_by_name['stream'].message_type = _RESPONSESTREAM
_QUERYPAYLOAD.fields_by_name['countRequest'].message_type = _COUNTREQUEST
_QUERYPAYLOAD.fields_by_name['countResponse'].message_type = _COUNTRESPONSE
_QUERYPAYLOAD.fields_by_name['endStream'].message_type = _ENDSTREAMREQUEST
_QUERYPAYLOAD.fields_by_name['streamEnd'].message_type = _STREAMENDRESPONSE
_STATISTICSREQUEST.fields_by_name['span'].message_type = _SPAN
_STATISTICSRESPONSE.fields_by_name['stats'].message_type = _INDEXSTATISTICS
_STATISTICSRESPONSE.fields_by_name['err'].message_type = _ERROR
_SCANREQUEST.fields_by_name['span'].message_type = _SPAN
_RESPONSESTREAM.fields_by_name['indexEntries'].message_type = _INDEXENTRY
_RESPONSESTREAM.fields_by_name['err'].message_type = _ERROR
_STREAMENDRESPONSE.fields_by_name['err'].message_type = _ERROR
_COUNTRESPONSE.fields_by_name['err'].message_type = _ERROR
_SPAN.fields_by_name['range'].message_type = _RANGE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['QueryPayload'] = _QUERYPAYLOAD
DESCRIPTOR.message_types_by_name['StatisticsRequest'] = _STATISTICSREQUEST
DESCRIPTOR.message_types_by_name['StatisticsResponse'] = _STATISTICSRESPONSE
DESCRIPTOR.message_types_by_name['ScanRequest'] = _SCANREQUEST
DESCRIPTOR.message_types_by_name['ScanAllRequest'] = _SCANALLREQUEST
DESCRIPTOR.message_types_by_name['EndStreamRequest'] = _ENDSTREAMREQUEST
DESCRIPTOR.message_types_by_name['ResponseStream'] = _RESPONSESTREAM
DESCRIPTOR.message_types_by_name['StreamEndResponse'] = _STREAMENDRESPONSE
DESCRIPTOR.message_types_by_name['CountRequest'] = _COUNTREQUEST
DESCRIPTOR.message_types_by_name['CountResponse'] = _COUNTRESPONSE
DESCRIPTOR.message_types_by_name['Span'] = _SPAN
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
DESCRIPTOR.message_types_by_name['IndexEntry'] = _INDEXENTRY
DESCRIPTOR.message_types_by_name['IndexStatistics'] = _INDEXSTATISTICS

class Error(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ERROR
  
  # @@protoc_insertion_point(class_scope:q2i.Error)

class QueryPayload(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYPAYLOAD
  
  # @@protoc_insertion_point(class_scope:q2i.QueryPayload)

class StatisticsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATISTICSREQUEST
  
  # @@protoc_insertion_point(class_scope:q2i.StatisticsRequest)

class StatisticsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATISTICSRESPONSE
  
  # @@protoc_insertion_point(class_scope:q2i.StatisticsResponse)

class ScanRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCANREQUEST
  
  # @@protoc_insertion_point(class_scope:q2i.ScanRequest)

class ScanAllRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCANALLREQUEST
  
  # @@protoc_insertion_point(class_scope:q2i.ScanAllRequest)

class EndStreamRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENDSTREAMREQUEST
  
  # @@protoc_insertion_point(class_scope:q2i.EndStreamRequest)

class ResponseStream(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSESTREAM
  
  # @@protoc_insertion_point(class_scope:q2i.ResponseStream)

class StreamEndResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMENDRESPONSE
  
  # @@protoc_insertion_point(class_scope:q2i.StreamEndResponse)

class CountRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COUNTREQUEST
  
  # @@protoc_insertion_point(class_scope:q2i.CountRequest)

class CountResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COUNTRESPONSE
  
  # @@protoc_insertion_point(class_scope:q2i.CountResponse)

class Span(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SPAN
  
  # @@protoc_insertion_point(class_scope:q2i.Span)

class Range(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RANGE
  
  # @@protoc_insertion_point(class_scope:q2i.Range)

class IndexEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INDEXENTRY
  
  # @@protoc_insertion_point(class_scope:q2i.IndexEntry)

class IndexStatistics(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INDEXSTATISTICS
  
  # @@protoc_insertion_point(class_scope:q2i.IndexStatistics)

# @@protoc_insertion_point(module_scope)
