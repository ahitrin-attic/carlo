import random
import string


INT_TYPE = 1
STR_TYPE = 2


def int_val(fixed_value=None):
    return (INT_TYPE, lambda: fixed_value)


def string_val(fixed_value=None, length=None, prefix=None, fn=None):
    if fixed_value:
        return (STR_TYPE, lambda: fixed_value)
    if fn:
        return (STR_TYPE, fn)
    if length is None:
        length = 10
    if prefix:
        length -= len(prefix)
        assert length >= 0
    else:
        prefix = ''
    return (STR_TYPE, lambda: prefix + ''.join(random.choice(string.letters) for _ in range(length)))


def time_val():
    pass
