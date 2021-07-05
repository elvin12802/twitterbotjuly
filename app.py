import tweepy
import time

consumer_key = '0llZZyMKfpYQYNFrVdPgYib3v'
consumer_secret = 'yImgAuGQwBnHeRAuIfOXzageySSPT6tvlOEmbKlTi9QoqNUsdI'
access_token = '1400467529663803396-4hYjuLjxBbwlXxprNjY24PsMv3kur9'
access_token_secret = '7bZKj3YHa60TMsa35rFwHHO9OVdGdnP7IkggHjM213j8s'

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

 
