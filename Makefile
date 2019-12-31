TEST_PATH=cabu
PIPENV_RUN=pipenv run

.SILENT: test clean-pyc clean-build isort lint install run

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	${PIPENV_RUN} sh -c "isort --skip-glob=.tox --recursive . "

lint:
	${PIPENV_RUN} autopep8 . -r --in-place
	-${PIPENV_RUN} pylint cabu

test: clean-pyc
	${PIPENV_RUN} python -m unittest discover -v $(TEST_PATH)

install:
	${PIPENV_RUN} install -r requirements.txt

run:
	python cabu/app.py
