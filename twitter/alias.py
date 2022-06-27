from enum import Enum


class TwitterAPI(str, Enum):
    '''
    Aliases for Twitter API constants.
    See https://developer.twitter.com/en/docs/twitter-api/
    '''

    BASE_URL = 'https://api.twitter.com/2'
    SEARCH_TWEETS_ENDPOINT = 'tweets/search/recent'
    RATE_LIMIT = 900  # 15 minutes
