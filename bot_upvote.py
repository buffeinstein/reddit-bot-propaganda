import praw
import random
import datetime
import time

from textblob import TextBlob

reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    user_agent='user_agent',
    username='username',
    password='password',
    )
reddit = praw.Reddit('bestbotintheworld999')

# submission_url = 'https://www.reddit.com/r/Liberal/comments/yzqnb4/i_understand_due_process_but_trump_continuing_to/'
# submission = reddit.submission(url=submission_url)

list_of_submissions = list(reddit.subreddit("cs40_2022fall").top(limit=100)) 
for submission in list_of_submissions: 
    if submission.url == 'https://www.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/':
        list_of_submissions.remove(submission)

#submission = random.choice(list_of_submissions)
vote_count = 0 

for submission in list_of_submissions: 
    print ('\n\n')
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list(): 
        all_comments.append(comment)
   # print('len(all_comments)=',len(all_comments))

    not_my_comments = []
    for comment in all_comments: 
        if comment.author == "bestbotintheworld999": 
            pass
        else: 
            not_my_comments.append(comment)
   # print('len(not_my_comments)=',len(not_my_comments))

    for comment in not_my_comments [:500]: 
        blob = TextBlob(comment.body)
        if "trump" in comment.body.lower(): 
            if blob.sentiment.polarity >0:
                comment.downvote()
                vote_count += 1
            else: 
                comment.upvote()
                vote_count += 1
    print ("vote count - ", vote_count)
    





