import praw
import random
import datetime
import time

import markovify

reddit = praw.Reddit('bestbotintheworld999')

with open("/Users/ambikatiwari/Downloads/CS40/GitHub/cs40project4/trumptext.txt") as f:
    text = f.read()

text_model = markovify.Text(text)


#THIS USES THE MARKOVIFY TO GENERATE MY COMMENT INSTEAD OF THE MADLIBS 
def generate_comment():
    return(text_model.make_short_sentence(280))

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    
    #1
    "[Donald Trump] has [understood] how [the world] works. Maybe because he has such [qualities] himself in [abundance], his appreciation for human [greed]  has given him a granite confidence in human corruptibility",
  #donald trump, understood, qualities, abundance, greed

   #2
    "[Mr Trump] [bullied] [senators] and [generals]. “You’re losers and you’re babies,” he told [America]’s military leaders, when they brought him to the Pentagon in an [attempt] to [persuade] him of the value of the post-war order. ",
  #mr trump, bullied, senators, generals, America, attempt, persuade
 
 #3
    "After the [2018 Florida high school shooting], [Trump] [met with] [parents] from the school and [promised] action on gun control. But [Trump] backed away after talking with [officials] from the National Rifle Association",
    #2018 Florida high school shooting, Trump, met with, parents, promised, Trump, officials

    #4
    "The Republicans are [looking] for someone to [blame], and [Donald Trump] has become the culprit-in-chief. Many of the far-right candidates he [endorsed] —mainly because they [echoed] his conspiracy theories—were defeated by more moderate Democratic opponents",
#looking, blame, Donald Trump, endorsed, echoed

    #5
    "[Mr Trump] made no [effort] to defend the Capitol. When his advisers [pleaded] with him to call off the rioters, he [angrily] [refused]",
    #Mr Trump, effort, pleaded, angrily, refused
    
    
    #6
    "A former lawyer, Ms Cheney [laid out] the case against [Mr Trump] in prosecutorial style. The [violent] insurrection after which the House committee is named, she said, was a [predictable] result of his [lie]" 
    #laid out, Mr Trump, violent, predictable, lie
        ]

replacements = {
    #every sentence has one of these three names
    'Donald Trump' : ['Donald Trump', 'Trump', 'Mr Trump'],
    'Trump' : ['Donald Trump', 'Trump', 'Mr Trump'],
    'Mr Trump' : ['Donald Trump', 'Trump', 'Mr Trump'],

#1:   #donald trump, understood, qualities, abundance, greed
    'understood' : ['comprehended', 'known', 'gotten', 'understood'],
    'greed' : ['cowardice', 'selfishness', 'greed', 'self-indulgence'],
    'the world' : ['society', 'life', 'politial sphere', 'the world'],
    'qualities' : ['traits', 'qualities', 'beliefs'],
    'abundance' : ['plenty', 'bounty'],

#2:   #mr trump, bullied, senators, generals, America, attempt, persuade

    'bullied': ['humiliated', 'degraded', 'disparaged', 'bullied'],
    'senators' :   ['politicians', 'political officials', 'lawmakers'],
    'generals' :  ['politicians', 'political officials', 'lawmakers'],
    'America' : ['America', 'USA'],
    'attempt' : ['effort', 'attempt', 'try'],
    'persuade' : ['convince', 'influence', 'persuade'],
 
 #3:  #2018 Florida high school shooting, Trump, met with, parents, promised, Trump, officials
    '2018 Florida high school shooting' : ['2018 Florida high school shooting', 'Florida high school shooting', 'high school shooting'],
    'met with' : ['spoke to', 'met with'],
    'parents' : ['parents', 'students', 'parents and students'],
    'officials' : ['political officials', 'spokespeople', 'officials'], 
    'promised' : ['assured', 'guaranteed', 'vowed', 'promised'],

    #4: #looking, blame, Donald Trump, endorsed, echoed

    'looking' : ['looking', 'searching', 'hunting'],
    'blame' : ['accuse', 'blame', 'point fingers at'],
    'endorsed' : ['supported', 'backed', 'endorsed'],
    'echoed' : ['supported', 'backed', 'endorsed'],

    #5:     #Mr Trump, effort, pleaded, angrily, refused
    
    'angrily' : ['furiously', 'indignantly'],
     'effort' : ['effort', 'attempt', 'try'],
     'pleaded' :  ['begged', 'implored'],
     'refused' : ['refused', 'denied'],
 

    #6:   #laid out, Mr Trump, violent, predictable, lie
    'violent' : ['brutual', 'hysterical', 'vicious', 'uncontrollable', 'violent'],
    'laid out' : ['argued', 'laid out', 'asserted'], 
    'predictable' : ['anticipated', 'predictable', 'forecastable'],
    'lie' : ['dishonesty', 'lie', 'fake stories', 'forgeries']
   
}


#THIS CODE GENERATES A COMMENT WITH THE MADLIBS FUNCTION 
'''
# def generate_comment():
#     
#     This function generates random comments according to the patterns specified in the `madlibs` variable.

#     To implement this function, you should:
#     1. Randomly select a string from the madlibs list.
#     2. For each word contained in square brackets `[]`:
#         Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
#     3. Return the resulting string.

#     For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
#     then the function might return "I like Python" or "I adore Programming".
#     Notice that the word "Programming" is incorrectly capitalized in the second sentence.
#     You do not have to worry about making the output grammatically correct inside this function.
#     Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
#     

#     madlib = random.choice(madlibs)
#     for replacement in replacements.keys():
#         madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
#     return madlib

'''


# FIXME:
# connect to reddit 

reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    user_agent='user_agent',
    username='username',
    password='password',
    )
reddit = praw.Reddit('bestbotintheworld999')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below

submission_url = 'https://www.reddit.com/r/Liberal/comments/yzqnb4/i_understand_due_process_but_trump_continuing_to/'
submission = reddit.submission(url=submission_url)


comment_count = 0
sleep_count = 0

while True:
    if comment_count >= 1000:
        break

    print ('\n\n')
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    all_comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list(): 
        all_comments.append(comment)
    print('len(all_comments)=',len(all_comments))


    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments: 
        if comment.author == "bestbotintheworld999": 
            pass
        else: 
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    comments_without_myreplies = []   
#POSTING A TOP LEVEL COMMENT IF I HAVE NOT REPLIED TO POST
    if has_not_commented:
        # FIXME (task 2)
        try: 
            submission.reply(generate_comment())
            print(datetime.datetime.now(), ': made a top-level comment')
            comment_count +=1 
        except (praw.exceptions.APIException):
            print ('sleeping for 5 secs')
            time.sleep(5)
           
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
    else:
        for comment in not_my_comments: 
            comment.replies.replace_more(limit=None) 
            comment_reply_authors =[]
            for reply in comment.replies.list(): 
                comment_reply_authors.append(reply.author)
            if "bestbotintheworld999" not in comment_reply_authors:
                comments_without_myreplies.append(comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_myreplies)=',len(comments_without_myreplies))

        # FIXME (task 4): randomly select a comment from the comments_without_myreplies list,
        # and reply to that comment

        #EXTRA CREDIT: RESPOND TO MOST UPVOTED COMMENT
        
        comments_without_myreplies_sorted = sorted(comments_without_myreplies, key=lambda x: x.score)
        
        try: 
            #random.choice(comments_without_myreplies).reply(generate_comment())
            #^ this was task 4

            #below is the code for extra credit - responding to the most upvoted comment in the chain
            comments_without_myreplies_sorted[-1].reply(generate_comment())
            #^ comment out this line if you want to 
            #QQ: is it ok if we let it run over and over, bc then it will not add the most upvoted 
            #comment if youve already responded to it to the comment_without_my_replies 
            #but thats only if you have already responded to the most upvoted
            #so it goes down the list of most upvoted
            #which ensures that youve got the most most upvoted in the comments that youve responded to 

            print(datetime.datetime.now(), ': replied to the most upvoted comment')
            comment_count +=1 
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
                    sleep_count += 1
                    print ("sleep count = ", sleep_count)
        except IndexError: 
            pass


# FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions

    # submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yyqwqx/test8/'
    # submission = reddit.submission(url=submission_url)

    list_of_submissions = list(reddit.subreddit("cs40_2022fall").top(limit=10)) 
    # #for submission in list_of_submissions: 
    #     if submission_url == 'https://www.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/':
    #         list_of_submissions.remove(submission)
    submission = random.choice(list_of_submissions)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)
