class TwitterError(Exception):
    '''
    Exception raised by failing to access Twitter API
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class UnauthorizedError(TwitterError):
    '''
    Exception raised when Twitter API doesn't accept passed token
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
