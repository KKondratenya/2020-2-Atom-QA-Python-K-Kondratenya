import pytest


@pytest.mark.parametrize("i", range(5))
def test_add(i):
    test_set = {i}
    test_set.add(i)
    assert len(test_set) == 1 and i in test_set


def test_remove(random_value):
    test_set = {random_value}
    test_set.remove(random_value)
    assert len(test_set) == 0


def test_remove_with_key_error(random_value):
    test_set = set()
    with pytest.raises(KeyError):
        test_set.remove(random_value)


def test_clear():
    test_set = {1, 2, 3, 4, 5}
    test_set.clear()
    assert len(test_set) == 0


class TestSet:

    def test_intersection(self):
        test_set1 = {1, 2, 3}
        test_set2 = {3, 4, 5}
        test_set3 = set.intersection(test_set1, test_set2)
        assert len(test_set3) == 1 and 3 in test_set3
