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
        

from calculators.hvl_tvl import (
    calculate_after_layers,
    calculate_layers,
)

def test_one_hvl():
    assert calculate_after_layers(100, 1, "HVL") == 50

def test_two_hvls():
    assert calculate_after_layers(100, 2, "HVL") == 25

def test_one_tvl():
    assert calculate_after_layers(100, 1, "TVL") == 10

def test_two_tvls():
    assert calculate_after_layers(100, 2, "TVL") == pytest.approx(1)

def test_hvl_case_insensitive():
    assert calculate_after_layers(100, 1, "hvl") == 50

def test_tvl_case_insensitive():
    assert calculate_after_layers(100, 1, "tvl") == 10

def test_zero_layers():
    assert calculate_after_layers(100, 0, "HVL") == 100

def test_required_hvls():
    assert calculate_layers(100, 50, "HVL") == pytest.approx(1)

def test_required_tvls():
    assert calculate_layers(100, 10, "TVL") == pytest.approx(1)

def test_required_two_hvls():
    assert calculate_layers(100, 25, "HVL") == pytest.approx(2)

def test_required_two_tvls():
    assert calculate_layers(100, 1, "TVL") == pytest.approx(2)

def test_negative_layers():
    with pytest.raises(ValueError):
        calculate_after_layers(100, -1, "HVL")

def test_invalid_layer_type():
    with pytest.raises(ValueError):
        calculate_after_layers(100, 1, "ABC")

def test_zero_initial_value():
    with pytest.raises(ValueError):
        calculate_layers(0, 10, "HVL")

def test_zero_final_value():
    with pytest.raises(ValueError):
        calculate_layers(100, 0, "HVL")

def test_final_greater_than_initial():
    with pytest.raises(ValueError):
        calculate_layers(50, 100, "HVL")