# EC601-Project2

# Phase A Twitter API
Twitter is like a huge gold mine for data analysers. Unlike the other social media, private and protective，Twitter's posts is open to nearly all users. If I want to grab some data to have some research on it or using method in data science, a large quantity of information from Twitter could be very helpful and benificial. For exmaple, to analyse the public attitude towards a university, I extracting the posts which is related to in recent time period, and then using NLP algorithms analyse them.

In my program, I import tweepy to get access to twitter's posts and other function of Twitter API. 

`api.home_timeline()`
could print out my account's timeline of the post.  Clearly I don't have any posts.

`api.update_status()`
could send a new post using my account. My account send a new post: hello python (I delete this post on my twitter.).

`api.user_timeline(id= , count= )`
allow me to review certain user's latest 'count'th posts. I get BU_Tweets's latest 20 posts.

`api.search(q= ,)` and `tweepy.Cursor(api.search, q= )`
could search for "q" as keyword. I search for Boston University

# Phase B Google Natural Language Api
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
