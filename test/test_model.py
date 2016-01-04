# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import Model, ModelException
import pytest

def test_minimal_model():
    m = Model(('const', {'int': lambda: 42})).build()
    assert [('const', {'int': 42})] == m.create()
    m = Model(('const2', {'str': lambda: 'hello'})).build()
    assert [('const2', {'str': 'hello'})] == m.create()

def test_model_with_multiple_entities():
    m = Model(
            ('first', {'name': lambda: 'elves'}),
            ('second', {'name': lambda: 'humans'})).build()
    assert [('first', {'name': 'elves'}),
            ('second', {'name': 'humans'})] == m.create()

def test_model_with_multiple_params():
    m = Model(('human', {
        'head': lambda: 1,
        'hands': lambda: 2,
        'name': lambda: 'Hurin',
        })).build()
    assert [('human', {'head': 1, 'hands': 2, 'name': 'Hurin'})] == m.create()

# error handling

def test_same_enitities_should_throw_error():
    with pytest.raises(ModelException):
        Model(('first', {'int': lambda: 32}),
              ('first', {'it works': lambda: False})).build()
