install:
	pip install --upgrade --no-cache-dir pip -r requirements-dev.txt

test:
	python -m unittest -qvb

cov:
	coverage run --source project -m unittest -qvb
	coverage report
	coverage html -d coverage/html
	coverage xml -o coverage/cobertura.xml
	coverage erase

isort:
	isort -rc project
	isort -rc tests
	isort -rc gunicorn.config.py
	isort -rc main.py

lint: isort

build:
	docker build . -t test_image:latest -f dockerfile

all: install lint test cov build

.PHONY: install cov isort lint build all

.DEFAULT_GOAL := all
