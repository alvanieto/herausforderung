from setuptools import setup, find_packages


def requirements_file(filename='requirements.txt'):
    '''read a requirements file and create a list that can be used in setup.

    '''
    with open(filename, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]


setup(
    name='herausforderung',
    version='0.0.1',
    author='Álvaro Nieto',
    author_email='alvaro.nieto@gmail.com',
    description='Data POI-Adquisition merge',
    packages=find_packages(),
    install_requires=requirements_file(),
    tests_require=['pytest', 'coverage']
)
