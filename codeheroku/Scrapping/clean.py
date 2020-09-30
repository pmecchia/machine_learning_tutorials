import pandas as pd
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords


stop_words = stopwords.words("english")


df=pd.read_csv("tweets.csv", encoding="utf-8")
print(df.shape)

def cleanData(tweet_text):
    #Task 1: Remove all retweet etxt of pattern : RT @Username:
    clean_text = re.sub(r'RT\s@\w+:\s',"", tweet_text)
    #Task 2: Remove all places where @Username appears in the string
    clean_text = re.sub(r'@\w',"",clean_text)
    #Task 3: Remove all hyperlinks
    clean_text= re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})','',clean_text)

    word_list = word_tokenize(clean_text)

    clean_list=[]

    for word in word_list:
        if word.isalpha() and word not in stop_words:
            clean_list.append(word)

    return " ".join(clean_list)

print("Before: ",df.iloc[23]["text"])

df["text"]=df["text"].apply(cleanData)

print("After: ",df.iloc[23]["text"])
