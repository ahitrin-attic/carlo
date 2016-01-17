import random
import string


INT_TYPE = 1
STR_TYPE = 2


def int_val(fixed_value=None):
    return (INT_TYPE, lambda: fixed_value, None)


def string_val(fixed_value=None, length=None, prefix=None, fn=None):
    def rnd_str(str_len):
        return lambda: prefix + ''.join(random.choice(string.letters) for _ in range(str_len))

    if fixed_value:
        return (STR_TYPE, lambda: fixed_value, None)
    if fn:
        return (STR_TYPE, fn, None)
    if prefix:
        assert length > 0
        length -= len(prefix)
        assert length >= 0
    else:
        prefix = ''
    if length is None:
        return (STR_TYPE, rnd_str(10), None)
    return (STR_TYPE, rnd_str(length), length)


def time_val():
    pass
