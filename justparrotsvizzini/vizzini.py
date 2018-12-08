import praw, time, calendar
from vizzinilines import lines

starttime = calendar.timegm(time.gmtime())

botname = "vizzini"
reddit = praw.Reddit(botname, user_agent='justparrotsvizzini')
subreddit = reddit.subreddit('popular')

print("Ready to begin.")
for comment in subreddit.stream.comments():
	if comment.author != reddit.user.me() and starttime <= comment.created_utc:
		print("New comment found at " + str(calendar.timegm(time.gmtime())))
		for key in lines.keys():
			if key in comment.body.lower() and starttime <= comment.created_utc:
				print("Responding...")
				comment.reply(">" + key + "\n\n" + lines[key])
		
