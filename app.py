import tweepy
import time
import os  # to get variables from config var in settings

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("Authentication Approved")
while True:
  user = api.get_user('@jstlketht1')
  u = user.followers_count
  api.update_profile(name=f'@jstlketht {u} Followers bot')
  print(f'@jstlketht {u} Followers bot')
  time.sleep(60)

 
