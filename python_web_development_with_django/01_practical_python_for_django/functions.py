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


# P.41
def daily_sales_total(*all_sales):
    total = 0.0
    print "type(all_sales):", type(all_sales)
    for each_sale in all_sales:
        total += float(each_sale)
    return total

print daily_sales_total(10, 10.11)


# P.42
bobargs = dict((f + '__contains', 'bob') for f in ('title', 'subtitle', 'text', 'byline'))


def filter(**bobargs):

    print bobargs
    print type(bobargs)

filter(**bobargs)