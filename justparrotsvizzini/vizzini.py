import praw, time, calendar
from vizzinilines import lines

starttime = calendar.timegm(time.gmtime())

reddit = praw.Reddit(user_agent='JustParrotsVizzini v0.1',
                  client_id='IxSfcfeoTZ6smw',
                  client_secret='IyvhSuN8SbehN9kEBtVxIz-_Bbg',
                  username='JustParrotsVizzini',
                  password='')

subreddit = reddit.subreddit('princessbridebots')

for comment in subreddit.stream.comments():
	if comment.author != reddit.user.me():
		for key in lines.keys():
			if key in comment.body.lower() and starttime <= comment.created_utc:
				print("New comment found! Responding...")
				comment.reply(lines[key])
		