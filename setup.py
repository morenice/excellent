from setuptools import setup
from setuptools import find_packages


setup(name='excellent',
        version='0.1',
        description='Excel third-party extensions',
        author='morenice',
        author_email='hyoungguyo@hotmail.com',
        url='https://github.com/morenice/excellent.git',
        license='MIT',
        install_requires=['xlrd'],
        packages=find_packages())
