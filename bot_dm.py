import praw
import random
import datetime
import time

import markovify

with open("/Users/ambikatiwari/Downloads/CS40/GitHub/cs40project4/trumptext.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

#THIS USES THE MARKOVIFY TO GENERATE MY COMMENT INSTEAD OF THE MADLIBS 
def generate_comment():
    return(text_model.make_short_sentence(280))

reddit = praw.Reddit('bestbotintheworld999')
#print(generate_comment())

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below

for i in range(100):
    try:
        reddit.redditor("botbombdotcom0").message(message=generate_comment(),subject="hi")
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
                time.sleep(delay)
            elif subexception.error_type == 'INVALID_USER':
                print ("wtf")
            else:
                print("Unknown error")
