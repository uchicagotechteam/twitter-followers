import tweepy
from tweepy import Cursor
import time
import json

consumer_key = 'p8rnniy2PVcnQR7I01s71g'
consumer_secret = 'tLaYYeiXzkq1wDmS2gEHTSEArNxk8tSd4D3bQPX6FNM'
access_token = '1196322271-BN4pBpveJuKSfUscrwss7T7KckX0Mgv75vJoVfp'
access_token_secret = 'A4yooP5jkdUfqI1xMi7wzVi9XtCh8uwScrPvOZyXR4nTz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

rep_cursor = Cursor(api.followers, id="repcurrie")

for page in rep_cursor.pages():
    try:
        print len(page)
        for user in page:
            user_str = str(user)
            username = user_str.split(", 'screen_name': ")[1].split(", '")[0]
            print username
        time.sleep(5)
    except BaseException, e:
        print "failed: ", str(e)
        time.sleep(10)
    
print "done pulling"
