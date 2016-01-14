# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import string_val
import pytest


def value_of(str_gen):
    assert str_gen[0] == 'str'
    return str_gen[1]()


class TestStringGenerator(object):
    def test_fixed_value(self):
        assert value_of(string_val('hello')) == 'hello'

    def test_given_length(self):
        assert len(value_of(string_val(length=10))) == 10
        assert len(value_of(string_val(length=42))) == 42

    def test_given_length_and_prefix(self):
        val = value_of(string_val(length=15, prefix='so good '))
        assert len(val) == 15
        assert val.startswith('so good ')

        val = value_of(string_val(length=5, prefix='hello'))
        assert len(val) == 5
        assert val.startswith('hello')

    def test_incorrect_length_and_prefix(self):
        with pytest.raises(AssertionError):
            value_of(string_val(length=1, prefix='oh wait!'))
