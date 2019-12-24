import re
import tweepy

# keys and tokens from Twitter
from tweepy import OAuthHandler


class TwitterClient(object):

    consumer_key = 'bNZYgGb8eqNeT68wfDoHeB8ed'
    consumer_secret = 'ySCJ1JQxWIdowa9MY3t7ypobdiF2WgusBOV10Urt3aFQodk5IO'
    access_token = '1605220128-d3UWnkknbp8nQ4S4uDU6rpye1gHGi4LtVJlLbld'
    access_token_secret = 'Timl9zqGcT0qUUldE9jglNxhu20LuUa8nbXvBo4dWIUt2'


    def __init__(self):
        '''
        class constructor or initialization method.
        '''

        # keys and tokens from Twitter
        consumer_key = 'bNZYgGb8eqNeT68wfDoHeB8ed'
        consumer_secret = 'ySCJ1JQxWIdowa9MY3t7ypobdiF2WgusBOV10Urt3aFQodk5IO'
        access_token = '1605220128-d3UWnkknbp8nQ4S4uDU6rpye1gHGi4LtVJlLbld'
        access_token_secret = 'Timl9zqGcT0qUUldE9jglNxhu20LuUa8nbXvBo4dWIUt2'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)

        except:
            print('Error: Authentication failed')


    def clean_tweet(self, tweet):
        ''' Utility
        function to clean tweet text by removing links, special characters using
        simple regex statements
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


    def get_tweets(self, query):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = 100)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = []

                # saving text of tweet
                parsed_tweet = tweet.text

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print('Error: ' + str(e))