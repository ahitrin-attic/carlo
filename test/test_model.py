# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import model, entity, generate

def test_minimal_model():
    m = model(entity('const', {'int': lambda: 42})).build()
    assert [('const', {'int': 42})] == m.create()
    m = model(entity('const2', {'str': lambda: 'hello'})).build()
    assert [('const2', {'str': 'hello'})] == m.create()

def test_model_with_multiple_entities():
    m = model(
            entity('first', {'name': lambda: 'elves'}),
            entity('second', {'name': lambda: 'humans'})).build()
    assert [('first', {'name': 'elves'}),
            ('second', {'name': 'humans'})] == m.create()
