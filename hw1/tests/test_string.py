import pytest


def test_find():
    test_string = '12'
    result = test_string.find('1')
    assert result == 0


def test_replace():
    test_string = '12'
    result = test_string.replace('1', '2')
    expected = '22'
    assert result == expected


def test_add():
    test_string1 = '12'
    test_string2 = '34'
    result = test_string1 + test_string2
    expected = '1234'
    assert len(result) == 4 and result == expected


def test_sub():
    test_string1 = '12'
    test_string2 = '34'
    with pytest.raises(TypeError):
        test_string1 - test_string2


class TestString:

    @pytest.mark.parametrize("i", range(10))
    def test_mul(self, i):
        result = f'{i}'*3
        expected = f'{i}{i}{i}'
        assert len(result) == 3 and result == expected
