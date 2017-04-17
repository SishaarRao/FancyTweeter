#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sishaarSecret import THESAURAS_KEY
# from secret import THESAURAS_KEY
import urllib.request
import re
import lxml.etree as ET

def parse(KEYWORD):
    req = urllib.request.Request('http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/'+KEYWORD+'?key='+THESAURAS_KEY)
    try:
        html = urllib.request.urlopen(req).read()
    except Exception as e:
        print(e)
        exit(0)

    print(html)

    try:
        if "<sn>" not in str(html):
            root = ET.fromstring(html)[0][2][2].text.split(",")
        else:
            root = ET.fromstring(html)[0][2][3].text.split(",")
        print(root)
        print(max(root, key=len))
    except IndexError as e:
        print("Not a valid entry")
        exit(0)
parse("because")
