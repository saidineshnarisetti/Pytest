# Any pytest file shouls start with "test_" or ends with "_test"
# test methods also starts with test_
# Any code should be wrapped in method only
# -k: This option specifies that you want to run tests whose names match the given string or expression
# -v: This option stands for "verbose" and makes the test output more detailed by displaying additional information.
# -s: This option captures and displays the standard output of the tests while they are running.
# -m: To run smoke tests, you can use the -m option followed by the marker name. For example, to run all smoke tests:
# you can skip test cases using @pytest.mark.skip
# @pytest.mark.xfail : Expect failure test cases and ignore it in test results:
# fixtures are used as setup and tear down methods for test cases -- conftest file is used to generalize
# fixture and make it available to all the test cases
#data driven and parameterization can be done with return statements in tuple formate
# when you define fixtures scope to class only, it will run once before class is initiated and at the end
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello Folks")

def test_secondMethod():
    print("Welcome to pytest learnings!")

