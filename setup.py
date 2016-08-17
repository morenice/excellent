from setuptools import setup
from setuptools import find_packages
import excellent


setup(name='excellent',
      version=excellent.__version__,
      description=excellent.__doc__.strip(),
      author='morenice',
      author_email='hyoungguyo@hotmail.com',
      url='https://github.com/morenice/excellent.git',
      license=excellent.__license__,
      packages=find_packages(),
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Software Development',
                   'Topic :: Utilities'
                   ]
      )
