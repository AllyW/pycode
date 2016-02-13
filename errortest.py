#! /usr/bin/python
# Filename: errortest.py

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something : ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException: this input was length %d, \
            was expecting at least %d' % (x.length, x.atleast)
else:
    print 'No exception was raised.'

