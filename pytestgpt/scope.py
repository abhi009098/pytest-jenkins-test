import pytest

@pytest.fixture(scope="function")
def my_fixture():
    return [1, 2, 3]

def test_function1(my_fixture):
    assert my_fixture == [1, 2, 3]

def test_function2(my_fixture):
    assert my_fixture == [1, 2, 3]




@pytest.fixture(scope="module")
def my_fixture_module():
    print("Setup code")
    yield
    print("Teardown code")


def test_one(my_fixture_module):
    print("Test one code")


def test_two(my_fixture_module):
    print("Test two code")

