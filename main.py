import sys
from itertools import cycle

try:
    assert sys.argv[1:]
    print(sum(c * int(x) for x, c in zip(sys.argv[1:], cycle([1, -1]))))
except AssertionError:
    print("NO PARAMS")
except Exception as e:
    print(e.__class__.__name__, e)
