import configparser
import tweepy 
import datetime

def validate(date_text):

        datetime.datetime.strptime(date_text,'%Y-%m-%d')
        print("True date")
        return True
    

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()

# def options(argument):
#     switcher = {
#         0 : "Merch",
#         1 : "Tour",
#         2: "Album" ,
#         3 : "dates",
#         4: "streams"
#     }
#     return switcher.get(argument, "nothing") #nothing here is the default value

# val = options(4)

val = input("Enter a keyword: ")

for tweet in public_tweets: 
    if val.casefold() in tweet.text:
        if(validate(val)):
            print(f"{tweet.user.name} said {tweet.text}")
            print(tweet.user.name)
            print(tweet.text)
