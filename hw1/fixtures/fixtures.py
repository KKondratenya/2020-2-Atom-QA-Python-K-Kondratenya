import random
import pytest


@pytest.fixture()
def random_value():
    yield random.randint(1, 1000)
