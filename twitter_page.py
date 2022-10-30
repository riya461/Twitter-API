
import configparser
import tweepy 

# def validate(date_text):

#         datetime.datetime.strptime(date_text,'%Y-%m-%d')
#         print("True date")
#         return True
  
def str_append(s, n,output):
    
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output

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



month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    
    

def month_acess(mon,val):
    for tweet in public_tweets: 
        if val.casefold() in tweet.text:
            
                if mon in tweet.text:
                    res = tweet.text.index(mon)
                    lenm = len(mon)
                    spaceindex1 = res+lenm+1 # index of the space 
                    spaceindex2 = res
                    print(spaceindex2)
                    print(tweet.text[spaceindex2-2])
                    prival = ''
                    if tweet.text[spaceindex1].isnumeric() :
                        
                        vale = tweet.text[spaceindex1:]
                        # print(mon)
                       
                        for i in vale:
                            
                            
                            if(i.isnumeric()):
                                prival = str_append(i,1,prival)
                            else:
                                break
                        
                        
                    
                        
                    elif tweet.text[spaceindex2-2].isnumeric():
                        
                        prival = ''
                        vale = tweet.text[spaceindex1:]
                        # print(mon)
                       
                        for i in vale:
                            
                            
                            if(i.isnumeric()):
                                prival = str_append(i,1,prival)
                            else:
                                break
                            
                        
                        
                    print(f"Date {prival} {mon}")
                    print(f"User: {(tweet.user.name)}")
                    print("Tweet: ")
                    print(tweet.text)
                    print(" ")
for i in month:                 
    month_acess(i,'') 
    
value = input("The month to be searched for results: ") 
month_acess(value,'')

key = input("a specific keyword: ")
month_acess(value,key)
  
                    
                        
                            
                        
                

# for tweet in public_tweets: 
#     print(tweet.text)
