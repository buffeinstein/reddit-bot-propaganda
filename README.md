# cs40project4


My bot is anti-Trump. 
Here is a link to one of my favorite comment threads that my bot responded to:
https://www.reddit.com/r/cs40_2022fall/comments/yz0j52/comment/ixkwx4y/?utm_source=share&utm_medium=web2x&context=3

I think the "whyyyyyyy" is funny, and I like that my bot is working properly. 

![Screen Shot 2022-11-27 at 9 41 49 PM](https://user-images.githubusercontent.com/108768418/204231409-9db50c99-692a-4bb6-8719-03a265ddf962.png)

Here is the output of running bot counter: 

```
limit =  1000
len(comments)= 1000
len(top_level_comments)= 0
len(replies)= 1000
len(valid_top_level_comments)= 0
len(not_self_replies)= 1000
len(valid_replies)= 1000
========================================
valid_comments= 1000
========================================
```

I completed all 6 tasks in the bot.py file.  = 12
Additionally, I completed my github repo.  = 3
I got 1000 valid comments for my first bot. = 10

My bot also creates new submissions, as coded in the botsubmissions.py. By running this file, you get 200 posts, 
which are all different. Some are text posts, and some are link posts. = 2

My bot will respond to the most upvoted comments. I have included a screenshot of running my bot, only once, on another subreddit that actually had a variety of votes on the comments, unlike most of the submissions in our subreddit. = 2

My bot also upvotes all commments that have match a negative sentiment on Trump, using the TextBlob sentiment analysis library, as seen in bot_upvote.py. = 4

I also trained a Markovify model with an Economist article that critizes Trump and the insurrection, which generates the text of my comments. = 5

Additionally, I created my own extra credit assignment to DM users using the generated text from Markovify, coded in bot_dm.py. I got a QCL tutor to agree to be the recipients of these comments. = 2
Here is the image he sent me of the dms that he was getting: 
![image](https://user-images.githubusercontent.com/108768418/206263910-87f8597d-ab3c-493f-a6bd-f37caec4a89a.png)


Total points: 40





