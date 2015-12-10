#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    pametis version 0.2 - Sitemap Analyzer/Parser
#    Copyright (c) 2015 Avner Herskovits
#
#    MIT License
#
#    Permission  is  hereby granted, free of charge, to any person  obtaining  a
#    copy of this  software and associated documentation files (the "Software"),
#    to deal in the Software  without  restriction, including without limitation
#    the rights to use, copy, modify, merge,  publish,  distribute,  sublicense,
#    and/or  sell  copies of  the  Software,  and to permit persons to whom  the
#    Software is furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this  permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT  WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE  WARRANTIES  OF  MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR  ANY  CLAIM,  DAMAGES  OR  OTHER
#    LIABILITY, WHETHER IN AN  ACTION  OF  CONTRACT,  TORT OR OTHERWISE, ARISING
#    FROM,  OUT  OF  OR  IN  CONNECTION WITH THE SOFTWARE OR THE  USE  OR  OTHER
#    DEALINGS IN THE SOFTWARE.
#

#
# Imports - stdlib
#
from gzip import decompress
from urllib. request import urlopen
import xml. etree. ElementTree as ET

NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'

#
# Use:
#
# from pametis import sitemap
# for url in sitemap( 'http://example.com/sitemap.xml' ):
#     ... do something with url ...
#
# This function will yield all sitemap leafs, recursing into nested sitemaps
# and decompressing gziped sitemaps.
#
def sitemap( url ):
    map = urlopen( url )
    inpstr = map. read()
    if url. endswith( '.gz' ):
        xmlstr = decompress( inpstr ). decode( 'utf-8' )
    else:
        xmlstr = inpstr. decode( 'utf-8' )
    xml = ET. fromstring( xmlstr )
    inp, xmlstr = None, None
    map. close()
    for child in xml:
        # Namespaced sitemap
        if NS + 'sitemap' == child. tag:
            for loc in child. iter( NS + 'loc' ):
                yield from sitemap( loc. text )
        elif NS + 'url' == child. tag:
            for loc in child. iter( NS + 'loc' ):
                yield loc. text
        # Namespaceless sitemap
        elif 'sitemap' == child. tag:
            for loc in child. iter( 'loc' ):
                yield from sitemap( loc. text )
        elif 'url' == child. tag:
            for loc in child. iter( 'loc' ):
                yield loc. text

#
# Can be used also as a command line utility, will print to stdout every leaf
# in the sitemap.
#
def _usage():
    print( '''\
pametis OPTIONS|<url>
Prints all the leaf urls in the sitemp.xml pointed to by <url>.

OPTIONS:
-h or --help Show This help message
''' )

def main():
    from sys import argv, stdout
    if 2 != len( argv ):
        _usage()
        exit( 1 )
    elif '-h' == argv[ 1 ] or '--help' == argv[ 1 ]:
        _usage()
        exit( 0 )
    else:
        for i in sitemap( argv[ 1 ]):
            print( i. encode( 'utf-8' ). decode( stdout. encoding ))

if '__main__' == __name__:
    main()
