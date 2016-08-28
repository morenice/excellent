.PHONY : all clean tests install uninstall

MODULE_NAME=excellent
VERSION=$(shell grep __version__ $(MODULE_NAME)/__init__.py | awk '{print $$3}' | sed -e s/\'//g)
PYTHON=python3
PIP=pip3

all : tests

run :
	@$(PYTHON) excellent.py

init :
	@echo "Inatll requirements ..."
	@$(PIP) install -r requirements.txt

tests :
	@echo "Running tests $(MODULE_NAME) $(VERSION) ..."
	@$(PYTHON) -m unittest discover -v

install :
	@echo "Install $(MODULE_NAME) ..."
	$(PYTHON) setup.py build
	$(PYTHON) setup.py install

uninstall :
	@echo "Uninstall $(MODULE_NAME) ..."
	$(PYTHON) setup.py install --record uninstall.txt
	cat uninstall.txt | xargs rm -rf

clean :
	@(cd excellent; rm -f *.pyc)
	@(cd tests; rm -f *.pyc)
	@(rm -rf build/ dist/ *.egg-info/)
