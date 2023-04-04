import pytest

@pytest.mark.smoke
def test_new1():
      print("perform 1st test")

@pytest.mark.smoke
def test_new2():
      print("perform 2nd test")

@pytest.mark.regression
def test_heavy_computation():
    print("perform 3rd test")



@pytest.mark.skip
@pytest.mark.parametrize("x,y", [(1, 2), (3, 4)])
def test_add(x, y):
    assert x + y == 5



@pytest.mark.parametrize("username", [
    "user1",
    "user2",
    "user3",
    "user4",
    "user5"
])
def test_username(username):
    # Your test code here
    print(f"Testing with username: {username}")



@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3"),
    ("user4", "pass4"),
    ("user5", "pass5")
])

def test_credentials(username, password):
    # Your test code here
    print(f"Testing with username: {username} and password: {password}")

