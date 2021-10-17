import tweepy

auth = tweepy.OAuthHandler('YnNRpoxFqfVnaUPXVrH7rJ8qP', 'A1tbq1Jst181Z60StvqE7w24G9CZKqkWy9fr4tRWAgiAXaZTIP')
auth.set_access_token('1732311679-15HQbpoZiwmedPZsrTpMDinfwQ96GKro9TfJUWT', 'ZRwZj42zUCRo8wEM5LpAwzbVWgfrpu1TOtXCBpY9Dse7P')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)