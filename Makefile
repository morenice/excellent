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
	#TODO
	@echo "Install $(MODULE_NAME) ..."

uninstall :
	#TODO
	@echo "Uninstall $(MODULE_NAME) ..."

clean :
	@(cd excellent; rm -f *.pyc)
	@(cd tests; rm -f *.pyc)

