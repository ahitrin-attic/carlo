import random
import string


def int_val(fixed_value=None):
    return ('int', lambda: fixed_value)


def string_val(fixed_value=None, length=None, prefix=None, fn=None):
    if fixed_value:
        return ('str', lambda: fixed_value)
    if fn:
        return ('str', fn)
    if length is None:
        length = 10
    if prefix:
        length -= len(prefix)
        assert length >= 0
    else:
        prefix = ''
    return ('str', lambda: prefix + ''.join(random.choice(string.letters) for _ in range(length)))


def time_val():
    pass
