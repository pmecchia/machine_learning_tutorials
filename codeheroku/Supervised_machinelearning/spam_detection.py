import pandas as pd
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

stop_words = stopwords.words("english")

df=pd.read_csv("ham_spam.csv",encoding='latin',index_col=False)
df = df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'], 1)
df.columns=['isSpam','email']
df["isSpam"]= df["isSpam"].replace("ham", 0)
df["isSpam"]= df["isSpam"].replace("spam", 1)

def cleanData(email_text):

    word_list = word_tokenize(email_text)

    clean_list=[]

    for word in word_list:
        if word.isalpha() and word not in stop_words:
            clean_list.append(word)

    return " ".join(clean_list)

df["email"]=df["email"].apply(cleanData)

x=df["email"]
y=df["isSpam"]

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

cv = CountVectorizer()
train_features=cv.fit_transform(X_train).toarray()
test_features=cv.transform(X_test).toarray()

model = GaussianNB().fit(train_features,y_train)

predictions=model.predict(test_features)

acc = metrics.accuracy_score(y_test,predictions)
print("predictions:", predictions)
print("accuracy: ", acc)
