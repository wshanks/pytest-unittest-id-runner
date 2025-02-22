# pytest-unittest-id-runner

This project provides a simple pytest plugin that converts unittest-style test identifiers into pytest-style test identifiers when passed as `file_or_dir` arguments to `pytest` on the command line.
This plug allows the following

    pytest path.to.test_file.TestClass.test_method

to be used instead of

    pytest path/to/test_file.py::TestClass::test_method

## Installation

The plugin can be installed with:

    pip install pytest-unittest-id-runner

Once installed, the plugin automatically attempts to perform the test identifier conversion without further configuration.

## Motivation

This plugin fills a fairly specific niche.
There are some projects out there that use unittest for testing instead of pytest, but they use unittest in a straightforward way, so that pytest can run the tests with its unittest compatibility support.
When working on such a project, one may prefer to work with the tests locally using pytest.
One motivation for doing this could be using a particular pytest feature or plugin for debugging test failures, since the pytest ecosystem is much bigger than unittest's.
In this case, one will find that the tests are run in CI with unittest and the failures are printed in the unittest style.
With `pytest-unittest-id-runner` installed, one can simply copy and paste the unittest identifiers from the CI output onto a pytest command line in order to debug the tests locally and not worry about converting between unittest and pytest styles of test identifier.
