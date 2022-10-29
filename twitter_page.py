from cgitb import text
import configparser
import tweepy 

# def validate(date_text):

#         datetime.datetime.strptime(date_text,'%Y-%m-%d')
#         print("True date")
#         return True
    

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweepy.Cursor(api.search, q="#hashtag", count=5, include_entities=True)
# if 'media' in public_tweets.entities:
#     for image in  tweet.entities['media']:
#         (do smthing with image['media_url'])
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

month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    

# val = input("Enter a keyword: ")

for tweet in public_tweets: 
    # if val.casefold() in tweet.text:
        for mon in month:
            if mon in tweet.text:
                res = tweet.text.index(mon)
                lenm = len(mon)
                spaceindex = res+lenm+1 # index of the space 
                print(res)
                print(spaceindex)
                
                print(f"{tweet.user.name} said {tweet.text}")
                print(tweet.user.name)
                val = tweet.text[spaceindex:]
                print(mon)
                print(val[:(val.index('.'))]) 
                # if(tweet.text[spaceindex].isnumeric()):
                #     # val = tweet.text[spaceindex]
                #     print(tweet.text[tweet.text[spaceindex]:val.index(' ')])                    
                #     print(f"Date{mon} {date_val}" )

# for tweet in public_tweets: 
#     print(tweet.text)
