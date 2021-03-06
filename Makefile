.PHONY: develop test test_coverage all install

all: develop

install:
	sudo apt-get update
	sudo apt-get install bedtools
	sudo apt-get install zlib1g-dev
	pip install -r requirements.txt
	python setup.py install

develop:
	sudo apt-get update
	sudo apt-get install bedtools
	sudo apt-get install zlib1g-dev
	pip install -r requirements.txt
	python setup.py develop

test:
	python setup.py test

test_coverage:
	python setup.py test -a '--cov=./src -v tests/'
