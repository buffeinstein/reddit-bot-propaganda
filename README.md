# cs40project4

1) bot.py - complete tasks.

2) let bot run continuously starting on 21 November until 28 November. 

3) Create a github repo for this project. The repo should contain:
- Your completed bot.py file **(but not your praw.ini file!!!).**


- A README.md file, properly formatted with markdown syntax, that:

I am supporting politician _____. 

Here is link to my favorite thread involving my bot
- an image screenshot of the thread
- and a short description of what i like about it. 
- ?? = (Below each comment is a button labeled permalink that lets you link to a comment.)


Includes the output of running the bot_counter.py file on your bot to count how many comments you've created. The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation).

Explains what you believe your score should be. Clearly state which tasks you complete/don't complete.
Grading rubric
The assignment is worth 30 points total.

Required Tasks
The following tasks are required, and total 20 points:

Each task in bot.py is worth 3 points. (6 tasks * 3 points/task = 18 points)

The github repo is worth 2 points.

Optional Tasks
In order to earn full credit on the assignment, you will have to complete some of the optional tasks. There are many of these optional tasks, and so it is possible to earn significant extra credit on this assignment.

You earn 2 points of extra credit for each of the following tasks you complete.

Getting at least 100 valid comments posted.

Getting at least 500 valid comments posted.

Getting at least 1000 valid comments posted.

Make your bot create new submission posts instead of just new comments. You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub. I recommend creating a separate python file for creating submissions and creating comments.

For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts. Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count.

You must create a new file bot_submissions.py and place all of the code in this new file. You should not modify the bot.py file to create submissions.

Create an "army" of 5 bots that are all posting similar comments. This will require creating 5 different reddit accounts. You can use the same code for each bot (but different praw.ini files with the corresponding login credentials). The challenge is keeping all 5 of these bots running simultaneously. Each bot needs to post at least 500 valid comments to get this extra credit.

Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible. You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like).

You must create a separate python file bot_vote.py for performing the upvotes. This file must loop over all submissions in the class subreddit and perform the up/down voting on all comments in each submission.

You may earn an additional two points if you use the TextBlob sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate. If the comment/submission has positive sentiment, then upvote it; if the comment/submission has a negative sentiment, then downvote it.

This extra credit is "grayhat" since it may violate reddit's TOS if not done correctly.

Your code must run on at least 100 submissions and all of the comments within those submissions (up to 500 comments total per submission) for the full extra credit. Not all of these submissions/comments need to be upvoted if they do not match your particular criteria for voting.

You earn 5 points of extra credit for each of the following tasks you complete.

Use a more sophisticated algorithm for generating the text of your comments. There are good python interfaces to the GPT-2 text generation algorithm, like gpt-2-simple, but they can be a bit finicky to get working well. The Markovify library provides an easier to use algorithm that's better than the MadLibs algorithm from lab, but not as good as GPT-2. If you're interested in trying for this extra credit, I'd be happy to discuss how to do this in office hours.
You may additionally propose more extra credit tasks that you would like to complete.

Negative Points
There are many ways to lose points on this assignment.

If your github repo contains any reddit credentials (e.g. a praw.ini file or passwords directly in the code), you will lose -25 points on the assignment.

If your bot posts to a subreddits not specifically designed for this course, you will lose -25 points on the assignment.

You may create your own subreddits for debugging purposes, and posting to these subreddits will not result in a point deduction.

If you lose enough points to go below 0 points, then you will receive negative points, and it would have been better to not complete the assignment at all.

Submission
Upload a link to your github repo to sakai.
