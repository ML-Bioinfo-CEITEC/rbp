.PHONY: develop test clean_python_cache all install

all: develop

install:
	sudo apt-get install zlib1g-dev
	sudo apt-get install bedtools
	pip install -r requirements.txt
	python setup.py develop

develop:
	python setup.py develop

test:
	python setup.py test

clean_python_cache:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
