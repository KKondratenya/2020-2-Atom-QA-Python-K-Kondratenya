import pytest


@pytest.mark.parametrize("i", range(5))
def test_add_key_and_value(i):
    test_dict = dict()
    test_dict[f'key{i}'] = i
    assert f'key{i}' in test_dict and test_dict[f'key{i}'] == i


def test_update_key():
    test_dict = {'key': 'value'}
    test_dict['key'] = 'value2'
    assert 'key' in test_dict and test_dict['key'] == 'value2'


def test_get():
    test_dict = {'key': 'value'}
    result = test_dict.get('key')
    assert result == 'value'


def test_get_with_default():
    test_dict = {'key': 'value'}
    result = test_dict.get('key2')
    assert result is None


class TestDict:

    def test_pop(self):
        test_dict = {'key': 'value'}
        result = test_dict.pop('key')
        assert ('key' not in test_dict) and result == 'value'
