.PHONY: install test run

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s . -p "test.py"

run:
	python dodawanie.py
