class PaginatedAPI():
    '''
    A simple base class for paginated APIs consumers
    to reduce repetitive logs

    :param log: Flag to toggle log
    :type log: bool
    :param log_every: A number for every how many pages should log
    :type log_every: int
    '''

    def __init__(self, log=False, log_every=1):
        ''' Constructor method '''
        self._log = log
        self._log_every = log_every

    def _should_log(self, page):
        '''
        Checks whether or not the given page should emit log

        :param page: Current page to number to be checked
        :type page: int
        :return: `True` if ``page`` number is
            divisible by ``log_every``, `False` otherwise
        :rtype: bool
        '''
        return self._log and page % self._log_every == 0

    def set_log(self, log):
        '''
        Sets ``log`` value

        :param log: New value to ``log``
        :type log: bool
        '''
        self._log = log

    def set_log_every(self, log_every):
        '''
        Sets ``log_every`` value

        :param log_every: New value to ``log_every``
        :type log_every: int
        '''
        self._log_every = log_every
