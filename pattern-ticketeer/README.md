# Code Refactoring Playground - Session 1

This is a guide for developers working on the Code Refactoring Playground
project. The project utilizes a Makefile to streamline various tasks related to
development and testing.

## Prerequisites

- You will need Linux or a Linux-Like environment.
- Make sure you have Python 3 installed on your system.
- Make sure you have Make installed on your system.

## Setting up the Development Environment

1. Clone the repository to your local machine.
2. Create a virtual environment using the following command:

```bash

make install
```

This command will create a Python virtual environment named venv and install the
required Python modules from the requirements.txt file.

## Running Unit Tests

To run the unit tests using pytest, execute the following command:

```bash

make test
```

This command will activate the virtual environment and run all the unit tests
located in the tests directory.

## Running Unit Tests with watch

To run the unit tests using ptw, execute the following command:

```bash

make ptw
```

This command will activate the virtual environment and run all the unit tests
located in the tests directory. It will then wait for files to change and
automatically re-run the tests.

## Running the Command-line Application

To run the command-line application, use the following command:

```bash

make run
```

This command will activate the virtual environment and execute the command-line
application. You can interact with the application through the terminal.

## Cleaning up the Development Environment

To clean up and remove the virtual environment, use the following command:

```bash

make clean
```

This command will remove the venv directory.

## Additional Notes

1. You can add python packages to the requirements.txt.
2. There is already a suite of unit test.
3. The `ticket` module is only partially complete.
