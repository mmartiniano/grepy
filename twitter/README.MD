# Twitter

After getting your own acess to [Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) you'll be ready to search for tweets.

## Requirements

On your [Python virtual environment](https://docs.python.org/pt-br/3/library/venv.html), run:

```pip install -r twitter/requirements.txt```

### Usage

By now, you can only **search recent tweets** (unfortunately no older then 7 days) that matches a query.

For instance, the code below greps tweets about "chilling capybaras":

```
from twitter import Twitter

twitter = Twitter('TWITTER_API_TOKEN')
query = '(chilling capybara) lang:en -is:retweet'

tweets = twitter.search_tweets(query)
for tweet in tweets:
    print(tweet['text'])
```

Instead of just iterating over tweets, you can also easily write them to a file:

```
from twitter import Twitter

twitter = Twitter('TWITTER_API_TOKEN', log=True)
query = '(chilling capybara) lang:en -is:retweet'

tweets = twitter.search_tweets(query)
writer('capybaras.csv', tweets)
```

To learn how to build a query that fits your needs, please check [this out](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).