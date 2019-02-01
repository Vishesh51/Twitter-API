import oauth2 as oauth
import json
import tweepy
import time
from tweepy import API
from tweepy import OAuthHandler

CONSUMER_KEY = "EJOg20WYarVTp868Qpdi1Eilq"
CONSUMER_SECRET = "F4FhyO0t7GnpDiWK4HSSft0cQSOdFlyJ7GmfjS7RZPpc3S59wW"
ACCESS_KEY = "838828921168752644-prxYkqDwsIkFpCRpgGEwJe7mJFpCfBr"
ACCESS_SECRET = "iRnlLV6WjiJ5kVddhIVWGg3VppBtaALQyjDOu0YlpfHQY"

auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
client=API(auth)

#profile=client.get_user(screen_name="_visheshsharma")
ids=[]
for page in tweepy.Cursor(client.friends_ids, screen_name="_visheshsharma").pages():
    ids.extend(page)
    #time.sleep(60)
	
ids1=[]
for page in tweepy.Cursor(client.followers_ids, screen_name="_visheshsharma").pages():
    ids1.extend(page)

print "Friends:\n"
print ids,"\n"

print "Followers:\n"
print ids1