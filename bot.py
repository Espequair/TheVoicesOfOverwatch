import sys,praw

args = sys.argv

my_user_agent = args[1]
my_client_id = args[2]
my_client_secret = args[3]
my_username = args[4]
my_password = args[5]

reddit = praw.Reddit(user_agent=my_user_agent,
			client_id=my_client_id,
			client_secret=my_client_secret,
			username=my_username,
			password=my_password)
 



subreddit = reddit.subreddit("all")
terms = ["audran is a imbec"]

for comment_id in subreddit.stream.comments():
	comment = reddit.comment(comment_id)
	text = comment_id.body.strip(" ?!.,").lower().encode('ascii','ignore')
	if text in terms:
		comment.reply("This worked!")
	print("Author: ",comment_id.author)
	print(text)
	print("---------------------------------------------------------")
