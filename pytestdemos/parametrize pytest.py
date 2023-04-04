import pytest


# #using fixtures parametrization
# @pytest.fixture(params=[1,2,3])
# def sample_fixture(request):
#     print(request.param)
#
# def test_example(sample_fixture):
#     print(sample_fixture)

# @pytest.mark.parametrize("a,b,final", [(1, 2, 3), (5, 5, 10), (6, 3, 11)])
# def test_add(a, b, final):
#     assert a + b == final

# @pytest.mark.parametrize("test_input,expected", [(1, 1),(2, 4),(3, 9)])
# def test_example(test_input, expected):
#     assert test_input ** 2 == expected

