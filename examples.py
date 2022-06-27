from util.csv import writer


### Twitter ###
from twitter import Twitter

# Get your own token
# https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
twitter = Twitter('<TWITTER_API_TOKEN>')

# Check tips for building a query
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
query = '(chilling capybara) lang:en -is:retweet'

# Get tweets no older then 7 days that matches query
tweets = twitter.search_tweets(query)
for tweet in tweets:
    print(tweet['text'])

# Or write them to file
tweets = twitter.search_tweets(query)
writer('capybaras.csv', tweets)
