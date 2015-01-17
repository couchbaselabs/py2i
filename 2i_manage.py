#!/usr/bin/env python
import requests
import json
from pprint import pprint, pformat
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument('-H', '--host', help="Admin port", default="localhost:9101")
ap.add_argument('-c', '--command', help="Command", choices=('list', 'drop', 'create'))
ap.add_argument('-n', '--name', help="Index Name", default=None)
ap.add_argument('-D', '--definition', help="Definition of a new index")
ap.add_argument('-B', '--bucket', help="Bucket for index", default="default")
ap.add_argument('-f', '--force', help="Force creation (Delete first)", default=True, action='store_true')
ap.add_argument('-T', '--type', help="Index type", choices=('lsm', 'ForestDB', 'gsi'), default='ForestDB')

options = ap.parse_args()

URLBASE = "http://{0}".format(options.host)
HEADERS = { 'content-type': 'application/json' }

def get_indexes():
    payload = { 'type': 'list' }
    payload = json.dumps(payload)
    r = requests.post(URLBASE+'/list', data=payload, headers=HEADERS)
    return r.json

def delete_index(namespec):
    ixlist = get_indexes()
    ixspec = find_index(ixlist, namespec)
    if ixspec is None:
        raise KeyError("No such index")

    for unused in ('using', 'expr', 'partnExpr', 'exprType'):
        ixspec.pop(unused, None)

    if True:
        payload = {'index': ixspec}
    else:
        payload = ixspec

    payload = json.dumps(payload)
    r = requests.post(URLBASE+"/drop", data=payload, headers=HEADERS)
    return r

def find_index(ixlist, spec):
    for d in ixlist['indexes']:
        print "Checking if {0} is in {1}".format(spec, pformat(d, indent=2))

        if 'defnID' in d and d['defnID'] == spec:
            return d
        if 'name' in d and d['name'] == spec:
            return d

    return None

if options.command == 'list':
    for ix in get_indexes()['indexes']:
        print "Have Index:"
        pprint(ix, indent=2)
        print ""

elif options.command == 'drop':
    if options.name is None:
        raise ValueError("Need name of index to drop")

    r = delete_index(options.name) 
    pprint(r.json, indent=2)

elif options.command == 'create':
    # ForestDB index
    if not options.definition:
        raise ValueError("Need definition for create!")
    if not options.name:
        raise ValueError("Need index name!")

    if options.force:
        try:
            delete_index(options.name)
        except KeyError:
            pass

    ixdef = {
            'name': options.name,
            'bucket': options.bucket,
            'using': options.type,
            'exprType': "N1QL",
            "secExprs": [options.definition],
            'isPrimary': False
    }
    ixdef = {'index': ixdef}
    ixdef = json.dumps(ixdef)
    r = requests.post(URLBASE+"/create", data=ixdef, headers=HEADERS)
    pprint(r.json, indent=2)
