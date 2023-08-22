import pytest
@pytest.mark.usefixtures("dataLoad")
class TestExampledataLoad:

    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print("This method will execute fixture demo method1")
        print(dataLoad[0])
        print(dataLoad[2])