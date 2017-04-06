#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sishaarSecret import THESAURAS_KEY
# from secret import THESAURAS_KEY
import urllib.request
import lxml.etree as ET

def main(KEYWORD):
    req = urllib.request.Request('http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/'+KEYWORD+'?key='+THESAURAS_KEY)
    try:
        html = urllib.request.urlopen(req).read()
#        with urllib.request.urlopen(req) as response:
#            html = response.read()
    except Exception as e:
        print(e)
        exit(0)

    print(html)
    root = ET.fromstring(html)[0][2][2].text.split(",")
    print(root)
main("hello")
