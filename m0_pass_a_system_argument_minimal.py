import sys

try:
    hell=sys.argv[1]
except IndexError:
    sys.argv = [
        __file__,
        'arg1',
        'arg2'
    ]
    hell = sys.argv[1]

print(hell)