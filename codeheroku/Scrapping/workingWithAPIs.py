import requests,json, tweepy,csv

#EXERCISE 1

API_KEY='28bda9fdd982562edfcaae3dc1c0baad'
base_url='https://api.openweathermap.org/data/2.5/weather'
payload={
    "q":"mumbai",
    "appid": API_KEY
}

response=requests.get(base_url,params=payload)
#my_dict=json.loads(response.text)
my_dict=response.json()
print(my_dict["weather"][0]["description"])

#EXERCISE 2

consumer_key = "K0cvlhlshR7SS4PVk6smJZqxG"
consumer_secret = "oCFV2iP3Nv1GxgahMIJbDoboFmCtLAFJXNB70e4lh3bwbu9IH7"

access_token = "1090590791750148096-6NuhCD8Lov29OQaE9UJpeQiTwX93iJ"
access_token_secret = "zO0JpF1LaXw3S09l6QndSMQOkRqI2mWgmUUNXHCa0otob"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.verify_credentials()

##Search for Acute Encephalitis Syndrome
search = api.search(q="Acute Encephalitis Syndrome",lang="en",rpp=100,count=100)
# for tweet in search:
# 	print(tweet.text,tweet.created_at,tweet.user.location)
file_out = open("tweets.csv","w+",encoding="utf-8")
writer = csv.writer(file_out)
writer.writerow(["created_at","screen_name","text"])

i = 0
for item in tweepy.Cursor(api.search,q="Encephalitis Syndrome").items(1000):
	print("Adding item",i,item.id)
	i+=1
	tweet = []
	tweet.append(item.created_at)
	tweet.append(item.user.screen_name)
	tweet.append(item.text)
	writer.writerow(tweet)

file_out.close()
