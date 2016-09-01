from setuptools import setup
from setuptools import find_packages
import os
import exceltp


SCRIPTS = ['bin/exceltp']

# On Windows we also need additional batch files to run the above scripts
if os.name == "nt":
    SCRIPTS += ['bin/exceltp.bat']

setup(name=exceltp.__module_name__,
      version=exceltp.__version__,
      description=exceltp.__doc__.strip(),
      author='morenice',
      author_email='hyoungguyo@hotmail.com',
      url='https://github.com/morenice/excellent.git',
      scripts=SCRIPTS,
      license=exceltp.__license__,
      packages=find_packages(),
      classifiers=[
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Software Development',
                   'Topic :: Utilities'
                   ]
      )
