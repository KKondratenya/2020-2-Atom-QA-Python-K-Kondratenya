import pytest


@pytest.mark.parametrize("i", range(10))
def test_append(i):
    test_list = []
    test_list.append(i)
    assert len(test_list) == 1 and test_list[-1] == i


def test_eq():
    test_list = [1, 2]
    test_list2 = [1, 2]
    assert test_list == test_list2


def test_add():
    test_list = [1, 2]
    test_list2 = [3, 4]
    result = test_list + test_list2
    expected = [1, 2, 3, 4]
    assert len(result) == 4 and result == expected


def test_sub():
    test_list = [1, 2]
    test_list2 = [3, 4]
    with pytest.raises(TypeError):
        test_list - test_list2


class TestList:

    def test_mul(self):
        result = [1]*3
        expected = [1, 1, 1]
        assert len(result) == 3 and result == expected
