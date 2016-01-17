import random
import string


INT_TYPE = 1
STR_TYPE = 2


def int_val(fixed_value=None):
    return (INT_TYPE, lambda: fixed_value, {'type': INT_TYPE})


def string_val(fixed_value=None, length=None, prefix=None, fn=None):
    def rnd_str(str_len):
        return lambda: prefix + ''.join(random.choice(string.letters) for _ in range(str_len))

    constraints = {'type': STR_TYPE}
    if fixed_value:
        return (STR_TYPE, lambda: fixed_value, constraints)
    if fn:
        return (STR_TYPE, fn, constraints)
    if prefix:
        assert length > 0
        length -= len(prefix)
        assert length >= 0
    else:
        prefix = ''
    if length is None:
        return (STR_TYPE, rnd_str(10), constraints)
    constraints['length'] = length
    return (STR_TYPE, rnd_str(length), constraints)


def time_val():
    pass
