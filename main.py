import tweepy
from textblob import TextBlob
import pandas as pd
from data_loader import load_and_clean_tweets
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt

#Twitter API authentication
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJ1C3gEAAAAAUh6Yc1OxDdROxRqyXlpDvAD2Qv8%3DJNgHaFohwJ0fHry2LEYbK8fpsixKqjAsBGcMn3acynPxwydkZq"
client = tweepy.Client(bearer_token=bearer_token)

#Search query
query = "Trump -is:retweet lang:en"

#Fetch tweets
tweets = client.search_recent_tweets(query=query, max_results=90)

#Process tweets
data = []
for tweet in tweets.data:
    analysis = TextBlob(tweet.text)
    data.append({
        "Tweet": tweet.text,
        "Polarity": analysis.sentiment.polarity,
        "Subjectivity": analysis.sentiment.subjectivity
    })
    
#Save to CSV 
df = pd.DataFrame(data)
df.index += 1  # start index from 1
df.to_csv("tweets.csv", index_label="Index")

tweets_df = load_and_clean_tweets("tweets.csv", save_cleaned=True)