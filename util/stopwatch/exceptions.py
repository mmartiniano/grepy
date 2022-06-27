class NotStoppedError(Exception):
    '''
    Exception thrown at attempting to retrieve :class:`util.StopWatch` result
    before stopping it
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
