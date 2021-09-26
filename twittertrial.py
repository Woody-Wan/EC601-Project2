import tweepy
consumer_key = "u7RcONIw4EVaP1rUh2bHFkOZR"
consumer_secret = "IoS5LwTGKoJkkI5gvC3GTHZysH2cqOTdKbs3XQ3Rxb8GE8mSVJ"
access_token = "1440734972394962946-TFX55WWuADSIvnSpkVmKIWbUCnBBxY"
access_token_secret = "IFyoL38xOpIfhUXQqFRTjU1grNBCNOtrK5APhNKFlWAAK"
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
query = "Toptal"
language = "en"
results = api.search(q=query,)
for tweet in results:
    print(tweet.user.screen_name,"Tweeted:",tweet.text)


for tweet in tweepy.Cursor(api.search, q='Boston University').items(10):
    print('Tweet by: @' + tweet.user.screen_name)

