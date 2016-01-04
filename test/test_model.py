# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import model, generate

def test_minimal_model():
    m = model(('const', {'int': lambda: 42})).build()
    assert [('const', {'int': 42})] == m.create()
    m = model(('const2', {'str': lambda: 'hello'})).build()
    assert [('const2', {'str': 'hello'})] == m.create()

def test_model_with_multiple_entities():
    m = model(
            ('first', {'name': lambda: 'elves'}),
            ('second', {'name': lambda: 'humans'})).build()
    assert [('first', {'name': 'elves'}),
            ('second', {'name': 'humans'})] == m.create()

def test_model_with_multiple_params():
    m = model(('human', {
        'head': lambda: 1,
        'hands': lambda: 2,
        'name': lambda: 'Hurin',
        })).build()
    assert [('human', {'head': 1, 'hands': 2, 'name': 'Hurin'})] == m.create()

# error handling

def test_same_enitities_should_throw_error():
    pass

def test_same_params_should_throw_error():
    pass
