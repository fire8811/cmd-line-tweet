import requests
import tweepy

'''
Apply for access to Twitters API here: https://developer.twitter.com/en/apply-for-access
'''

user = #your twitter username 

'''
Access your keys and tokens by going to the developer portal, then clicking
your dev profile name at the top > Apps > Details > Keys and Tokens

'''
key = #API key
secretKey = #API secret key 
accessToken = #Your access token 
accessToken_secret = #Your acess token secret

auth = tweepy.OAuthHandler(key, secretKey)
auth.set_access_token(accessToken, accessToken_secret)

api = tweepy.API(auth)

tweet = input('Enter tweet: ')
try:
    api.update_status(status=tweet)
    print('success')
    #you will then see your tweet in your profile
except:
    print('error')



