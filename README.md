# Configure the environment

## Prerequisites

* Python 3.7
* Tested only on Linux

## Development environment

I recommend to install the dependencies in a virtualenv.

```bash
python setup.py develop
```
or
```bash
pip install -r requirements.txt
```

## Running tests

All tests run with pytest (configuration in setup.cfg)

```bash
pytest tests
```

## Tests coverage

Coverage results in html are in htmlcov/index.html

## Run the application

```bash
python setup.py install
merge --help
```

To run the program with best normalize execute;

```bash
merge tests/acceptance/data_poi_part_1.csv tests/acceptance/data_poi_part_2.csv --alghoritm normalize_road
```
