import pytest

from calculators.dose_rate import (
    calculate_dose,
    calculate_dose_rate,
    calculate_time,
)


def test_calculate_dose():
    assert calculate_dose(2, 10) == 20


def test_calculate_dose_rate():
    assert calculate_dose_rate(20, 10) == 2


def test_calculate_time():
    assert calculate_time(20, 2) == 10


def test_zero_dose():
    assert calculate_dose(0, 10) == 0


def test_zero_time():
    assert calculate_dose(10, 0) == 0


def test_zero_dose_rate():
    assert calculate_dose_rate(0, 10) == 0


def test_negative_dose():
    with pytest.raises(ValueError):
        calculate_dose(-1, 10)


def test_negative_dose_rate():
    with pytest.raises(ValueError):
        calculate_dose_rate(-1, 10)


def test_negative_time():
    with pytest.raises(ValueError):
        calculate_time(10, -1)


def test_zero_time_for_dose_rate():
    with pytest.raises(ValueError):
        calculate_dose_rate(10, 0)


def test_zero_dose_rate_for_time():
    with pytest.raises(ValueError):
        calculate_time(10, 0)
        
from calculators.inverse_square import calculate_inverse_square


def test_inverse_square_double_distance():
    assert calculate_inverse_square(100, 1, 2) == 25

def test_inverse_square_half_distance():
    assert calculate_inverse_square(100, 2, 1) == 400

def test_inverse_square_same_distance():
    assert calculate_inverse_square(100, 5, 5) == 100

def test_inverse_square_quarter_distance():
    assert calculate_inverse_square(100, 1, 0.5) == 400

def test_inverse_square_zero_initial_value():
    assert calculate_inverse_square(0, 1, 2) == 0

def test_inverse_square_negative_initial_value():
    with pytest.raises(ValueError):
        calculate_inverse_square(-100, 1, 2)

def test_inverse_square_zero_initial_distance():
    with pytest.raises(ValueError):
        calculate_inverse_square(100, 0, 2)

def test_inverse_square_zero_new_distance():
    with pytest.raises(ValueError):
        calculate_inverse_square(100, 1, 0)

def test_inverse_square_negative_initial_distance():
    with pytest.raises(ValueError):
        calculate_inverse_square(100, -1, 2)

def test_inverse_square_negative_new_distance():
    with pytest.raises(ValueError):
        calculate_inverse_square(100, 1, -2)