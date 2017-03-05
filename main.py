#!/usr/bin/env python

import tweepy, time, sys, requests, threading
from KEYS_TOKENS import *
import get_image

random_url = get_image.get_random_url()
random_jpg = get_image.get_random_image_jpg(random_url)


def twitter_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def tweet_image(url):
    api = twitter_api()
    filename = 'temp_image.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status="#donaldtrump #tinytrump #maga #fact #trump @realDonaldTrump ")
        print('tweeted out image')
    else: 
        print('Unable to download image')
        
    
tweet_image(random_jpg)
