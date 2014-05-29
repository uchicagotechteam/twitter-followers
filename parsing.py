follower_file = open("currie_followers.json", 'r')

for user in follower_file.readlines():
    # checking if user has screen_name attribute
    if len(user.split("'screen_name'")) > 1:
        username = user.split("'screen_name'")[1].split(", u'")[0]
        print username
    else:
        print "user has no username"
    # checking if user has hashtags
    if len(user.split("'hashtags'")) > 1:
        hashtags = user.split("'hashtags'")[1].split("], u'")[0]
        print hashtags
    else:
        print "user has no hashtags"
