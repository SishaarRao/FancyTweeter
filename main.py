#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sishaarSecret import THESAURAS_KEY, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
# from secret import THESAURAS_KEY, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import urllib.request
import re
import lxml.etree as ET
from stop_words import get_stop_words
import tweepy, time, sys

USERNAME = "Sishaar_Rao_API"

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

def tweet(strInput):
    # Separate the input into words
    strInput = re.compile('[^a-zA-Z]').sub(' ', strInput).split()
    
    # Loop through the input and parse each word, disregarding articles or stop words
    stop_words = get_stop_words('english')
    articles = open("common_articles.txt").read().split()
    toTweet = ""
    for word in strInput:
        if word not in stop_words and word not in articles:
            toTweet += parse(word) + " "
        else:
            toTweet += word + " "
    return toTweet



# Create client
try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    
    client = tweepy.API(auth)
    if not client.verify_credentials():
        raise tweepy.TweepError

    USER = client.get_user(USERNAME)
    ID = USER.id_str
except tweepy.TweepError as e:
    print('ERROR : connection failed. Check your OAuth keys.')
    sys.exit(0)
else:
    print('Connected as @{}, you can start to tweet !'.format(client.me().screen_name))
    client_id = client.me().id
    

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        client.update_status("@" + status.user.screen_name + " "  + tweet(status.text.split(' ', 1)[1]), status.id_str)
        
    def on_error(self, status_code):
        if status_code == 420:
            return False

# Create Stream Listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = client.auth, listener=myStreamListener)

# Begin
myStream.filter(track=[USERNAME])

