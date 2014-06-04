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

rep_cursor = Cursor(api.followers, id='repcurrie')

outFile = open('currie_followers.json', 'w')

total_received = 0
for page in rep_cursor.pages():
	try:
		print len(page)
		num_followers = len(page)
		for follower in page:
			print type(follower)
			outFile.write('%s\n' % follower)
		total_received += len(page)
		outFile.write('%s\n' % page)
		time.sleep(5)
	except BaseException, e:
		print 'failed: ', str(e)
		time.sleep(10)
print 'done pulling'
print 'pulled ' +str(total_received) + ' followers'