dev: lint test

install_dev:
	pip install -r requirements_dev.txt

lint: install_dev
	pep8 .

# test targets
test: unittest

unittest: install_dev
	pytest --verbose tests
