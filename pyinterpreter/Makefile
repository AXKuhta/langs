
all: coverage

coverage:
	@python3 -m coverage run -m pytest tests/
	@python3 -m coverage report

html:
	@python3 -m coverage run -m pytest tests/
	@python3 -m coverage html
	@open htmlcov/index.html
