# EC601-Project2

# Phase A Twitter API
Twitter is like a huge gold mine for data analysers. Unlike the other social media, private and protective，Twitter's posts is open to nearly all users. If I want to grab some data to have some research on it or using method in data science, a large quantity of information from Twitter could be very helpful and benificial. For exmaple, to analyse the public attitude towards a university, I extracting the posts which is related to in recent time period, and then using NLP algorithms analyse them.

In my program, I import tweepy to get access to twitter's posts and other function of Twitter API. 

api.home_timeline() could print out my account's timeline of the post.  Clearly I don't have any posts.

api.update_status() could send a new post using my account. My account send a new post: hello python (I delete this post on my twitter.).

api.user_timeline(id= , count= ) allow me to review certain user's latest 'count'th posts. I get BU_Tweets's latest 20 posts.

api.search(q= ,) and tweepy.Cursor(api.search, q= ) could search for "q" as keyword. I search for Boston University
