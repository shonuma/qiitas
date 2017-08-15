# Python 3.5.2


class MyClass:
    def __init__(self, prefix='My'):
        self._prefix = prefix

    def my_method(self, x):
        return '{} {}'.format(self._prefix, x)
