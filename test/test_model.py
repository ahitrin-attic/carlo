# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import Model, ModelException, eq, int_val, string_val
import pytest

def test_minimal_model():
    m = Model(const={'int': int_val(42)}).build()
    assert [('const', {'int': 42})] == m.create()
    m = Model(const2={'str': string_val('hello')}).build()
    assert [('const2', {'str': 'hello'})] == m.create()

def test_model_with_multiple_entities():
    m = Model(first={'name': string_val('elves')},
              second={'name': string_val('humans')}).build()
    assert sorted([('first', {'name': 'elves'}),
                   ('second', {'name': 'humans'})]) ==\
           sorted(m.create())

def test_model_with_multiple_params():
    m = Model(human={
        'head': int_val(1),
        'hands': int_val(2),
        'name': string_val('Hurin'),
        }).build()
    assert [('human', {'head': 1, 'hands': 2, 'name': 'Hurin'})] == m.create()

# restrictions

def test_restriction_must_override_parameter_definition():
    m = Model(leader={'direction': string_val('north')},
              follower={'direction': string_val('west')},
        ).restricted_by(eq('leader.direction', 'follower.direction')).build()
    assert sorted([('leader', {'direction': 'north'}),
                   ('follower', {'direction': 'north'})]) == \
           sorted(m.create())
