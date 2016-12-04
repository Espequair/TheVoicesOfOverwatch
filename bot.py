import praw
import sys

args = sys.argv

my_user_agent = args[1]
my_client_id = args[2]
my_client_secret = args[3]
my_username = args[4]
my_password = args[5]

r = praw.Reddit(user_agent=my_user_agent,
                     client_id=my_client_id,	
                     client_secret=my_client_secret,
                     username=my_username,
                     password=my_password)
 
subreddit = r.subreddit("Overwatch")


for submission in subreddit.new(limit = 1):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    #print("Approved: ", submission.approve)
    print("Approved_by: ", submission.approved_by)
    print("Author: ", submission.author)
    print("Domain: ", submission.domain)
    print("Downs: ", submission.downs)
    print("Downvote: ", submission.downvote)
    print("Edit: ", submission.edit)
    print("Edited: ", submission.edited)
    print("Saved: ", submission.saved)
    print("Score: ", submission.score)
    print("Secure media: ", submission.secure_media)
    print("Secure media embed: ", submission.secure_media_embed)
    print("selftext: ", submission.selftext)
    print("Semftext html: ", submission.selftext_html)
    print("Ups: ", submission.ups)
    print("Upvote: ", submission.upvote)
    print("URL: ", submission.url)
    print("User_Reports: ", submission.user_reports)
    print("Visited: ", submission.visited)
    #print("Vote: ", submission.vote)
    print("---------------------------------\n")
