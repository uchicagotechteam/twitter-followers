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

outFile = open("currie_followers_badbadbad.json", 'w')

total_received = 0

for page in rep_cursor.pages():
    try:
        # tell us how many followers we have thus far
        total_received += len(page)
        print len(page)
        outFile.write("%s\n" % page)
        time.sleep(10)
    except BaseException, e:
        print "failed: ", str(e)
        time.sleep(20)

print "done pulling"
print "pulled " + str(total_received) + " follower"
