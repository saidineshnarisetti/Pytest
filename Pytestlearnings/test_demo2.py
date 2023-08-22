import pytest

# @pytest.mark.smoke
@pytest.mark.xfail
@pytest.mark.skip
def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hi", "Test case failed due to string do not match"

def test_forthProgram():
    a = 5
    b = 10
    assert a + 5 == b, "Addition matched, test case passed"

def test_fifthProgram():
    a = 22
    b = 10
    assert a - 13 == b, "Subtraction failed, test case failed"
