import tweepy
from tweepy import Cursor
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

rep_cursor = Cursor(api.followers, id="repcurrie")

outFile = open("followers_new.json",'w')

num_followers = 0

for page in rep_cursor.pages():
    try:
        print len(page)
        num_followers += len(page)
        for follower in page:
            print type(follower)
            outFile.write("%s\n" % page)
        time.sleep(10)
    except BaseException, e:
        print "failed: ", str(e)
        time.sleep(20)

print 'done pullin'
