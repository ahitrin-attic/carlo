#coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import generate


class FakeModel(object):
    def __init__(self, *events):
        self.events = events
        self.i = -1

    def create(self):
        if self.i < len(self.events) - 1:
            self.i += 1
        else:
            self.i = 0
        return self.events[self.i]


def test_fake_model_returns_given_events_in_loop():
    m = FakeModel([3, 2, 1], [5, 4], [6])
    assert [3, 2, 1] == m.create()
    assert [5, 4] == m.create()
    assert [6] == m.create()
    assert [3, 2, 1] == m.create()
    assert [5, 4] == m.create()


def test_generate_one_shot():
    m = FakeModel([('a', {'x': 2}),
                   ('b', {'y': 3, 'z': 4})],
                  [('a', {'x': 5})],
                  [('a', {'x': 6}),
                   ('b', {'y': 7, 'z': 8}),
                   ('b', {'y': 9, 'z': 10})])
    assert [('a', {'x': 2}),
            ('b', {'y': 3, 'z': 4})] == \
           generate(m, 1)


def test_generate_multiple_shots():
    m = FakeModel([('a', {'x': 2}),
                   ('b', {'y': 3, 'z': 4})],
                  [('a', {'x': 5})],
                  [('a', {'x': 6}),
                   ('b', {'y': 7, 'z': 8}),
                   ('b', {'y': 9, 'z': 10})])
    assert [('a', {'x': 2}),
            ('b', {'y': 3, 'z': 4}),
            ('a', {'x': 5}),
            ('a', {'x': 6}),
            ('b', {'y': 7, 'z': 8}),
            ('b', {'y': 9, 'z': 10}),] == \
           generate(m, 3)
