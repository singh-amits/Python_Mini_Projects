import tweepy

auth = tweepy.OAuthHandler('YnNRpoxFqfVnaUPXVrH7rJ8qP', 'A1tbq1Jst181Z60StvqE7w24G9CZKqkWy9fr4tRWAgiAXaZTIP')
auth.set_access_token('1732311679-15HQbpoZiwmedPZsrTpMDinfwQ96GKro9TfJUWT', 'ZRwZj42zUCRo8wEM5LpAwzbVWgfrpu1TOtXCBpY9Dse7P')

api = tweepy.API(auth)
user = api.me()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print(tweet.text)

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)
			
#genrous Bot
#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#for follower in tweepy.Cursor(api.followers).items():

	#print(follower.name)
search_string = 'python'
numbersofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersofTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
	    break	


