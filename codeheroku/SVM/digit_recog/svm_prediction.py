import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split


##Step 1: Get Data from CSV
df=pd.read_csv("csv/dataset.csv",index_col=False)

##Step 2: Seperate Labels and Features
X=df.drop(["label"],axis=1)
y=df["label"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

##Step 3: Make sure you have the correct Feature / label combination in training


##Step 4: Build a Model and Save it
model = svm.SVC(gamma="auto",kernel='linear')
model.fit(X_train,y_train)

joblib.dump(model,"model/svc_4digits")

##Step5 : Print Accuracy

predictions=model.predict(X_test)

acc = metrics.accuracy_score(y_test,predictions)

print(acc)
