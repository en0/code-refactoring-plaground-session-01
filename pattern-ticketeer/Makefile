# Makefile for Code Refactoring Playground

# Export the PYTHONPATH to make modules accessable
export PYTHONPATH=.

# Name of the virtual environment
VENV_NAME := venv

# Command to create the virtual environment
VENV := python3 -m venv $(VENV_NAME)

# Command to activate the virtual environment
ACTIVATE_VENV := . $(VENV_NAME)/bin/activate

# Install dependencies from requirements.txt
install:
	$(VENV)
	$(ACTIVATE_VENV); pip install -r requirements.txt

# Run unittests using pytest
test:
	$(ACTIVATE_VENV); pytest tests

# Run unittests using ptw
ptw:
	$(ACTIVATE_VENV); ptw

# Run the command line application
run:
	$(ACTIVATE_VENV); python -m ticket

# Clean up virtual environment
clean:
	rm -rf $(VENV_NAME)

.PHONY: install test run clean
