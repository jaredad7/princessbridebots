import praw, time, calendar

starttime = calendar.timegm(time.gmtime())

reddit = praw.Reddit(user_agent='JustParrotsVizzini v0.1',
                  client_id='IxSfcfeoTZ6smw',
                  client_secret='IyvhSuN8SbehN9kEBtVxIz-_Bbg',
                  username='JustParrotsVizzini',
                  password='asyouwish')

print(reddit.user.me())

subreddit = reddit.subreddit('princessbridebots')

for comment in subreddit.stream.comments():
	print(str(comment) + "\t" + str(comment.created_utc) + "\t" + str(starttime))
	if "dizzying intellect" in comment.body.lower() and starttime <= comment.created_utc:
		print("New comment!")
		comment.reply("Wait till I get going!\n\n...where was I?")
		