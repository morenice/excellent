.PHONY : all clean tests install uninstall

MODULE_NAME=excellent

VERSION=$(shell grep __version__ $(MODULE_NAME)/__init__.py | awk '{print $$3}' | sed -e s/\'//g)
PYTHON=python3

all : tests

tests :
	@echo "Running tests ..."
	@$(PYTHON) -m unittest discover -v

install :
	@echo "Install $(MODULE_NAME) ..."

uninstall :
	@echo "Uninstall $(MODULE_NAME) ..."

clean :
	@(cd excellent; rm -f *.pyc)
	@(cd tests; rm -f *.pyc)

