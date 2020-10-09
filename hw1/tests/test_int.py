import pytest


def test_add():
    assert 1 + 2 == 3


def test_sub():
    assert 2 - 1 == 1


def test_negative_int():
    test_int = 1
    result = -test_int
    assert result == -1


@pytest.mark.parametrize("value", [1, 0, -1])
def test_abs(value):
    if value >= 0:
        assert abs(value) == value
    else:
        assert abs(value) == -value


class TestInt:

    def test_div(self):
        assert 3 // 2 == 1
