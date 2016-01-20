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
              follower={'direction': string_val()},
        ).restricted_by(eq('leader.direction', 'follower.direction')).build()
    assert sorted([('leader', {'direction': 'north'}),
                   ('follower', {'direction': 'north'})]) == \
           sorted(m.create())

def test_two_strings_of_same_length_could_be_eq():
    m = Model(x={'a': string_val(length=4),
                 'b': string_val(length=4)}
        ).restricted_by(eq('x.a', 'x.b')).build()
    row = m.create()[0][1]
    assert row['a'] == row['b']

# error handling
@pytest.mark.parametrize('model,restrictions', [
    ({'leader': {'direction': string_val('north')}, 'follower': {'direction': int_val(13)}},
     [eq('leader.direction', 'follower.direction')]),
    ({'x': {'a': string_val(length=5), 'b': string_val(length=4)}},
     [eq('x.a', 'x.b')]),
])
def test_failure_on_bad_combinations(model, restrictions):
    m = Model(**model).restricted_by(*restrictions)
    with pytest.raises(ModelException):
        m.build()
