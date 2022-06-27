import requests
from http import HTTPStatus
from time import sleep

from util.stopwatch import Stopwatch
from base import PaginatedAPI
from twitter.alias import TwitterAPI
from twitter.exceptions import TwitterError, UnauthorizedError


class Twitter(PaginatedAPI):
    '''
    Twitter API consumer class

    :param token: A Twitter API Bearer token
    :type token: str
    '''

    def __init__(self, token, log=False, log_every=1):
        ''' Constructor method '''
        self._token = token
        super().__init__(log, log_every)

    def _auth_header(self):
        '''
        Retrieves a header with Bearer Token Authorization

        :raises: UnauthorizedError: Raised when ``_token`` attribute is falsy
        :return: Dict containing a Authorization header
        :rtype: dict
        '''

        if not self._token:
            raise UnauthorizedError('no twitter token')

        return {'Authorization': f'Bearer {self._token}'}

    def search_tweets(self, query, per_page=100, retry_after=None):
        '''
        Yields each tweet reached from search/recent endpoint that matchs given query.
        In order to get all matched tweets, this process might sleep to fit rate limits.
        See https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate

        :param query: Query to search tweets for.
            Check https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
        :type query: str
        :param per_page: Number of tweets to get for each page. Defaults to 100
        :type per_page: int, optional
        :param retry_after: Number of secods to wait when Twitter API rate limit is reached.
            Defaults to 900 (15 minutes).
            See https://developer.twitter.com/en/docs/twitter-api/rate-limits
        :type retry_after: int, optional
        :raises: UnauthorizedError: Raised when Twitter API returns HTTP 401 status code
        :raises: TwitterError: Thrown when Twitter API returns a HTTP status code other then 200, 401 or 429
        :return: A generator for each tweet reached
        :rtype: generator
        '''

        sleep_time = retry_after or TwitterAPI.RATE_LIMIT
        url = '/'.join((
            TwitterAPI.BASE_URL, TwitterAPI.SEARCH_TWEETS_ENDPOINT
        ))

        params = {
            'max_results': per_page,
            'query': query
        }

        next_page = None
        page = 0
        stopwatch = Stopwatch()

        print('searching recent tweets...')
        stopwatch.start()

        while True:
            next_page and params.update({'pagination_token': next_page})

            super()._should_log(page) and print(f'\tpage {page}')

            response = requests.get(
                url, params=params, headers=self._auth_header()
            )

            if response.status_code != HTTPStatus.OK:
                error = f'{response.status_code}: {(response.text or "").lower()}'

                if response.status_code == HTTPStatus.UNAUTHORIZED:
                    raise UnauthorizedError(error)

                if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
                    print(error)
                    print(f'retrying in {sleep_time}s')
                    sleep(sleep_time)
                    continue

                raise TwitterError(error)

            result = response.json()

            for tweet in result['data']:
                yield tweet

            page += 1
            next_page = result.get('meta', {}).get('next_token')

            if not next_page:
                stopwatch.stop()
                print(f'finished in {stopwatch.show()}')
                return
