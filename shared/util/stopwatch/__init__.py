from time import time, gmtime

from util.stopwatch.exceptions import NotStoppedError


class Stopwatch():
    '''
    The StopWatch object simply handles measuring something's duration.
    In this case, the time between the call of ``start`` and ``stop`` methods.
    The ``show`` method retrives the measurement result
    '''

    def __init__(self):
        ''' Constructor method '''
        self._start = None
        self._end = None
        self._result = None

    def start(self):
        ''' Starts time measurement '''
        self._start = time()
        self._end = None
        self._result = None

    def stop(self):
        ''' Stops time measurement '''
        self._end = time()
        self._result = self._end - self._start

    def show(self):
        '''
        Retrieves the measuring result.

        :raises: NotStoppedError: Thrown when the StopWatch wasn't stopped  yet
        :return: String containing the time measurement in terms of hours (h),
            minutes (m) and seconds (s)
        :rtype: str
        '''
        if not self._result:
            raise NotStoppedError('stopwatch is still running')

        return ' '.join((
            f'{value}{unity}'
            for value, unity in zip(
                (
                    getattr(gmtime(self._result), attr)
                    for attr in ('tm_hour', 'tm_min', 'tm_sec')
                ),
                ('h', 'm', 's')
            )
            if value
        ))
