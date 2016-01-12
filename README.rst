Carlo: describe a model and generate a list of events using this model
=====

    First of all he cut hairs on the log, then the forehead, the the eyes...

    Suddenly the eyes opened themselves and stared at him...

    Carlo gave no sign that he's frightened, just asked gently:

    – Wooden eyes, why do you look at me so strange?

    -- Aleksey Nikolaevich Tolstoy, "The Golden Key, or the Adentures of Buratino"

Although Papa Carlo was just a street organ player, his most famous achievement was creation of Buratino, speaking wooden doll. Using `carlo` you could also create (random) events following the described model.

Alpha version warning
---------------------

Current version is alpha only, all things may change in future: API, dependencies, and even the library's future is uncertain at this moment.

Example
-------

Image we want to create simple database containing information about photos of cats. Having two tables, ``cats`` and ``photos``, we want to generate **some amount of random data** for these tables. With ``carlo``, it could be done the following way::

    from carlo import *

    tables = Model(
        cats={
        'id': int_val(),
        'name': string_val(),
        'born': time_val(),
        },
        photos={
        'id': int_val(),
        'cat_id': int_val(),
        'taken': time_val(),
        }
    ).restricted_by(
        eq('cats.id', 'photos.cat_id'),
        ge('photos.taken', 'cats.born'),
        cardinal_many('cats', 'photos', 0, 10)
    ).build()

    generate(tables, 2)
    # which should produce:
    #
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

Please note that **actual** state of the library is quite far from the declared in the example. Following things **do not work** at the current moment:

 * any restrictions except ``eq``
 * cardinality restrictions
 * ``generate`` function
