# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import model, entity, generate

def test_minimal_model():
    m = model(entity('const', {'int': lambda: 42}))
    assert [('const', {'int': 42})] == m.create()
