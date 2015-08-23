#!/usr/bin/env python

import httplib

def check_web_server(host, port, path):
    h = httplib.HTTPConnection(host, port)
    h.request('GET', path)
    resp = h.getresponse()
    print 'HTTP Response:'
    print '    status =', resp.status
    print '    reason =', resp.reason
    print 'HTTP Headers:'
    for hdr in resp.getheaders():
        print '    %s: %s' % hdr

check_web_server('www.python.org', 80, '/')

