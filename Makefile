.PHONY: develop test clean_python_cache all

all: develop

develop:
	pip install -r requirements.txt
	python setup.py develop

test:
	python setup.py test

clean_python_cache:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
