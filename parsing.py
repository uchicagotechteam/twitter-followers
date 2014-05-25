follower_file = open("follower_lines.json", 'r')

for user in follower_file.readlines():
    username = user.split(", 'screen_name': ")[1].split(", '")[0]
    print username
    location = user.split(", 'location': ")[1].split(", '")[0]
    print location
