""" A Twitter Listener to seek tweets from specific users """

from pprint import pprint
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

# All those keys could ge obtained though your twitter account
consumer_key = "YOUR_CONSUMER_TWITTER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET_TWITTER_KEY"
access_token = "TWITTER_ACCESS_TOKEN"
access_token_secret = "TWITTER_ACCESS_SECRET_TOKEN"


class TwitterPeeker:
    def __init__(self):
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.auth_api = API(self.auth)

    def get_first_n_tweets(self, target_account, tweet_quantity):
        tweets = []
        for status in Cursor(self.auth_api.user_timeline, id=target_account).items(tweet_quantity):
            tweets.append(status.text)
        return tweets

if __name__ == "__main__":
    target_account = 'TheGentlebros'
    tweet_quantity = 10
    twitter_peeker = TwitterPeeker()
    pprint(twitter_peeker.get_first_n_tweets(target_account, tweet_quantity), indent=4)
