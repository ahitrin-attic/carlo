PRUNY: clean test2

default=all

clean:
	rm -rf .env2 .cache

.env2/bin/python2:
	virtualenv .env2 --py=/usr/bin/python2
	.env2/bin/pip install pytest

test2: .env2/bin/python2
	.env2/bin/py.test

all: test2
