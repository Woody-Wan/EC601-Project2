import tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# My own timeline
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
# send a new post on my account
api.update_status('hello python')


# Certain User's timeline
name = "BU_Tweets"
tweetCount = 20
results = api.user_timeline(id=name, count=tweetCount)
for tweet in results:
    print(tweet.text)

# Search for certain info in 2 ways
query = "Boston"
language = "en"
results = api.search(q=query,)
for tweet in results:
    print(tweet.user.screen_name,"Tweeted:",tweet.text)


for tweet in tweepy.Cursor(api.search, q='Boston University').items(10):
    print('Tweet by: @' + tweet.user.screen_name)

