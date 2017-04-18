#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sishaarSecret import THESAURAS_KEY
# from secret import THESAURAS_KEY
import urllib.request
import re
import lxml.etree as ET
from stop_words import get_stop_words

def parse(KEYWORD):
    # Request to the Thesauras API
    req = urllib.request.Request('http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/'+KEYWORD+'?key='+THESAURAS_KEY)
    try:
        html = urllib.request.urlopen(req).read()
    except Exception as e:
        print(e)
        exit(0)

    # Get the longest synonym
    try:
        if "<sn>" not in str(html):
            root = re.split(",| ", ET.fromstring(html)[0][2][2].text)
        else:
            root = re.split(",| ", ET.fromstring(html)[0][2][3].text)
        return max(root, key=len)
    except IndexError as e:
        # Not a valid entry
        return KEYWORD

# Separate the input into words
strInput = "I hate Donald Trump"
strInput = re.compile('[^a-zA-Z]').sub(' ', strInput).split()

# Loop through the input and parse each word, disregarding articles or stop words
stop_words = get_stop_words('english')
articles = open("common_articles.txt").read().split()
print(stop_words)
for word in strInput:
    if word not in stop_words and word not in articles:
        print(parse(word))
    else:
        print(word)
        
    
