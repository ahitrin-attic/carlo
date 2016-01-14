import random
import string


def int_val(fixed_value=None):
    return ('int', lambda: fixed_value)


def string_val(fixed_value=None, length=None, prefix=None):
    if fixed_value:
        return ('str', lambda: fixed_value)
    if prefix:
        length -= len(prefix)
    else:
        prefix = ''
    return ('str', lambda: prefix + ''.join(random.choice(string.letters) for _ in range(length)))


def time_val():
    pass
