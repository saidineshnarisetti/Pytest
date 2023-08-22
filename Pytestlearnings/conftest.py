import pytest

@pytest.fixture(scope="class")
def setup():
    print("This is the first message from setup!")
    yield
    print("This is the last message")
@pytest.fixture(scope="class")
def dataLoad():
    print("User profile data is being created")
    return ["saidinesh","Narisetti","https://medium.com/@saidinesh.narisetti"] # tupple
@pytest.fixture(params=[("chrome","Testdatavar1","Testdatavar2"), ("firefox","FFTestdata1","FFTetsdata2"), "ie"])
def crossBrowsers(request):
    return request.param
