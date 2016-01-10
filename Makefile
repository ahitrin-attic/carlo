.PHONY: clean test2

all: test2

clean:
	rm -rf .env2 .cache dist carlo/*.egg-info
	find . -name __pycache__ | xargs rm -rf

.env2/bin/python2:
	virtualenv .env2 --py=/usr/bin/python2
	.env2/bin/pip install -r requirements.txt
	.env2/bin/pip install -r requirements-dev.txt

test2: .env2/bin/python2
	.env2/bin/py.test
