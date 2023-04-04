import pytest


@pytest.mark.math
def test_m1():
    assert 1 == 1


def test_m2():
    name = "abhi"
    assert name.upper() == name



@pytest.mark.math
def test_m3():
    a = 1
    b = 3
    assert a + b == 4

@pytest.mark.math
def test_m4():
    assert 'apple' == "banana"