.PHONY: develop test clean_python_cache all install

all: develop

install:
	sudo apt-get update
	sudo apt-get install bedtools
	sudo apt-get install zlib1g-dev
	pip install -r requirements.txt
	python setup.py develop

develop:
	python setup.py develop

test:
	python setup.py test

test_coverage:
	python setup.py test -a '--cov=./src -v tests/'
