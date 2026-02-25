import pytest
from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(10, 20) == 40


def test_subtract(calc):
    assert calc.subtract(20, 10) == 10


def test_multiply(calc):
    assert calc.multiply(5, 4) == 20


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
