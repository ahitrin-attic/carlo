#!/usr/bin/env python2
# coding: utf-8

from carlo import *

tables = model(
    entity('cats', {
        'id': int_val(),
        'name': string_val(),
        'born': time_val(),
        }),
    entity('photos', {
        'id': int_val(),
        'cat_id': int_val(),
        'taken': time_val(),
        })
).restricted_by(
    eq('cats.id', 'photos.cat_id'),
    ge('photos.taken', 'cats.born'),
    cardinal_many('cats', 'photos', 0, 10)
).build()

generate(tables, 2)
# [('cats', {'id': 23424313434,
#            'name': 'cat',
#            'born': datetime(2001, 10, 13)}),
#  ('photos', {'id': 49345,
#              'cat_id': 23424313434,
#              'taken': datetime(2004, 1, 12)}),
#  ('photos', {'id': 3535209834399,
#              'cat_id': 23424313434,
#              'taken': datetime(2001, 12, 2)}),
#  ('photos', {'id': 33444,
#              'cat_id': 23424313434,
#              'taken': datetime(2011, 6, 7)}),
#  ('cats', {'id': 242431,
#            'name': 'sdf sffd',
#            'born': datetime(1912, 4, 12)}),
# ]
