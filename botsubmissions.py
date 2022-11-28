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
            try: 
                subreddit.submit(title, url=url)
                submission_count += 1
            except praw.exceptions.RedditAPIException as e:
                for subexception in e.items:
                    if subexception.error_type == "RATELIMIT":
                        error_str = str(subexception)
                        print(error_str)
                        if 'minute' in error_str:
                            delay = error_str.split('for ')[-1].split(' minute')[0]
                            delay = int(delay) * 60.0
                        else:
                            delay = error_str.split('for ')[-1].split(' second')[0]
                            delay = int(delay)  
                        print ("delay = ", delay, "at", datetime.datetime.now())
                        time.sleep(delay)     

        else: 
            subreddit = reddit.subreddit("cs40_2022fall")
            try: 
                subreddit.submit(title, selftext=selftext)
                submission_count += 1 
            except praw.exceptions.RedditAPIException as e:
                for subexception in e.items:
                    if subexception.error_type == "RATELIMIT":
                        error_str = str(subexception)
                        print(error_str)
                        if 'minute' in error_str:
                            delay = error_str.split('for ')[-1].split(' minute')[0]
                            delay = int(delay) * 60.0
                        else:
                            delay = error_str.split('for ')[-1].split(' second')[0]
                            delay = int(delay)  
                        print ("delay = ", delay, "at", datetime.datetime.now())
                        time.sleep(delay)        
        
    print (submission_count)

