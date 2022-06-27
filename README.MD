# Grepy

A Collection of Python modules for extracting data from online systems


## Twitter

After getting your own acess to [Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) you'll be ready to search for tweets.

For instance, the Python code below greps tweets about "chilling capybaras":

```
from twitter import Twitter

twitter = Twitter('TWITTER_API_TOKEN')
query = '(chilling capybara) lang:en -is:retweet'

tweets = twitter.search_tweets(query)
for tweet in tweets:
    print(tweet['text'])
```