def int_val(fixed_value=None):
    return ('int', lambda: fixed_value)

def string_val(fixed_value=None):
    return ('str', lambda: fixed_value)

def time_val():
    pass
