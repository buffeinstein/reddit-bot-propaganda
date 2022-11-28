import praw
import random
import datetime
import time

reddit = praw.Reddit('bestbotintheworld999')

submission_count = 0

for i in range(200): 
    list_of_submissions = list(reddit.subreddit("communist").hot(limit=200))
    for submission in list_of_submissions:
        title = submission.title
        selftext = submission.selftext

        if selftext == "":
            url = submission.url
            subreddit = reddit.subreddit('cs40_2022fall')
            subreddit.submit(title, url = url)
            submission_count += 1


        else: 
            subreddit = reddit.subreddit("cs40_2022fall")
            subreddit.submit(title, selftext=selftext)
            submission_count += 1     
               
    print (submission_count)

