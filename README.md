# EC601-Project2

# Phase 1A Twitter API
Twitter is like a huge gold mine for data analysers. Unlike the other social media, private and protective，Twitter's posts are open to nearly all users. If I want to grab some data to have some research on it or using method in data science, a large quantity of information from Twitter could be very helpful and benificial. For exmaple, to analyse the public attitude towards a university, I extracting the posts which is related to in recent time period, and then using NLP algorithms analyse them.

In my program, I import tweepy to get access to twitter's posts and other function of Twitter API. 

`api.home_timeline()`
could print out my account's timeline of the post.  Clearly I don't have any posts.

`api.update_status()`
could send a new post using my account. My account send a new post: hello python (I delete this post on my twitter.).

`api.user_timeline(id= , count= )`
allow me to review certain user's latest 'count' posts. I get BU_Tweets's latest 20 posts. 

`api.search(q= ,)` and `tweepy.Cursor(api.search, q= )`
could search for "q" as keyword. I search for Boston University， and return some posts that related to Boston University. It is like the search funtion in twitter web and app end.

# Phase 1B Google Natural Language Api
The Google Natural Language API is an easy-to-use interface to a set of powerful NLP models that have been trained by Google to perform a variety of tasks. Since these models have been trained on a very large corpus of documents, they typically perform well as long as they are used on datasets that do not use very specific languages.The biggest advantage of using these pre-trained models through the API is that no training dataset is required. The API allows the user to start making predictions immediately, which is valuable when there is little labeled data.

The Natural Language API contains five different services.

*Syntax analysis*

*Sentiment analysis*

*Entity Analysis*

*Entity sentiment analysis*

*Text classification*

Google's sentiment analysis will provide a mainstream sentiment perspective in the text provided.

The Score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall sentiment from the given information.

The Magnitude of the sentiment ranges from 0.0 to +infinity and indicates the overall strength of sentiment from the given information. The more information that is provided the higher the magnitude.

In this section , I tried 2 ways to use the Google Natural Language API. I used an interactive Python interpreter called IPython, which is preinstalled in Cloud Shell to perform Sentiment Analysis on a string and find out the Score and Magnitude using the Natural Language API. And I also download the credential in json format to perform Sentiment Analysis in Python.
```
text      : Guido van Rossum is great!
score     : 90.0%
magnitude : 90.0%
```
```
text      : You can use the AutoML UI to upload your training data and test your custom model without a single line of code.
score     : 50.0%
magnitude : 50.0%
```
```
text      : The White House said talks over twin bills that would revitalize the nation's roads and airports and fund social programs and climate change measures, were at a precarious point as moderates and progressives disagreed over the scope of some $4 trillion in spending.
score     : -70.0%
magnitude : 70.0%
```
Ipython Code:
```
from google.cloud import language


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")
```

# Phase 2 User Story
Since Twitter's posts are open to nearly all users, which could be a gread mine of data for people to dig the useful informaion. By accessing Twitter's API, it could allow me to search and pull down pieces of information on certain objects or issues, and then help me to place an assessment on them. In this case, I could use the analyse result to apply in my own app.

Analyzing sentiment regarding products and companies serves as a relatively new way to predict the products or companies that will be successful and those that won't. In addition, in can also serve as a new line to the customer to take feedback about what people liked about a product and what they didn't. Twitter sentiment can also be used to drive investment decisions, with companies that exhibit an increase in postive sentiment over time presumed to be better investments than an equal counterpart with a negative trend in sentiment.

For example, if I want to apply for a university that I do not know much about it, or I just heard of, and I need a more comprehensive reviews, what should I do? Well, Checking out the official website is definitely a good way to have a overall view on it, but the officilal definitely will not write out their shortcomings and drawbacks. Meanwhile, the rankings may be provide a standard for people to refer, but these rankings are too sketchy. If I could use a method or an app to by collecting people's reviews on that spot to generate a scores with pros and cons, then I could get a relatively more accurate and comprehensive overview on it, and this could save a lot of work.

In this case, I shall apply the .search() funtion of the API to get the close-related posts and the posts which contain the keyword I search for. Transforming the received data to the form that Google Natural Language API could accept and analyse, then I could get the score and magnitude of each post. By averaging the points that return, I could get an approximate review on the searched object.  

# Completion

To finish my app with mvp funtions, I combine 2 modules that I mentioned before. Getting data from website,  I use the Twitter API, extracting and searching for the keyworads that user requires. Then Twitter API could return the related data to my app. Using Google API, I import Google Natural Language to analyse the message received from Twitter. Google API send back the score and magnitude of each tweets, and to get the overall review on the 'keyword' object, I set the result as an average score of each message.
![image](https://user-images.githubusercontent.com/63642698/136701352-b6588112-3506-47d0-9135-9c327b436716.png)

```
Overall Sentiment: score of 78.6% with magnitude of 78.6%
```
