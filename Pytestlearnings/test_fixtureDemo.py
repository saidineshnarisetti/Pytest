# import pytest
# @pytest.fixture
# def setup():
#     print("This is the first message from setup!")
#     yield
#     print("This is the last message")
import pytest
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("This method will execute fixture demo method1")

    def test_fixtureDemo2(self):
        print("This method will execute fixture demo method2")

    def test_fixtureDemo3(self):
        print("This method will execute fixture demo method3")

    def test_fixtureDemo4(self):
        print("This method will execute fixture demo method4")
