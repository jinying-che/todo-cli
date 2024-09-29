venv:
	python3 -m venv .venv
	. .venv/bin/activate

build:
	pip install --editable .

