.PHONY : all claen tests

MODULE=excellent
VERSION=$(shell grep __version__ $(MODULE)/__init__.py)

all : tests


tests :
	@echo "Running tests ..."

