"""
Tests for the Medical Physics Unit Converter.
"""

import pytest

from converter import convert


def test_gy_to_rad():
    assert convert(1, "Gy", "rad") == 100

def test_rad_to_gy():
    assert convert(100, "rad", "Gy") == 1


def test_sv_to_rem():
    assert convert(1, "Sv", "rem") == 100

def test_rem_to_sv():
    assert convert(100, "rem", "Sv") == 1


def test_mev_to_kev():
    assert convert(1, "MeV", "keV") == 1000

def test_kev_to_mev():
    assert convert(1000, "keV", "MeV") == 1

def test_gev_to_ev():
    assert convert(1, "GeV", "eV") == 1e9

def test_ev_to_gev():
    assert convert(1e9, "eV", "GeV") == 1


def test_bq_to_ci():
    assert convert(3.7e10, "Bq", "Ci") == 1

def test_ci_to_bq():
    assert convert(1, "Ci", "Bq") == 3.7e10


def test_cm_to_m():
    assert convert(100, "cm", "m") == 1

def test_m_to_mm():
    assert convert(1, "m", "mm") == 1000

def test_mm_to_um():
    assert convert(1, "mm", "μm") == pytest.approx(1000)

def test_angstrom_to_nm():
    assert round(convert(1, "Å", "nm"), 12) == 0.1

def test_picometer_to_nm():
    assert round(convert(1, "pm", "nm"), 12) == 0.001
    
def test_kg_to_g():
    assert convert(1, "kg", "g") == 1000

def test_g_to_mg():
    assert convert(1, "g", "mg") == pytest.approx(1000)


def test_min_to_s():
    assert convert(1, "min", "s") == 60

def test_h_to_s():
    assert convert(1, "h", "s") == 3600

def test_day_to_h():
    assert convert(1, "day", "h") == 24


def test_same_unit():
    assert convert(5, "Gy", "Gy") == 5
    
    
def test_pressure_pa_to_kpa():
    assert convert(1000, "Pa", "kPa") == 1

def test_pressure_bar_to_pa():
    assert convert(1, "bar", "Pa") == 100000

def test_pressure_atm_to_pa():
    assert convert(1, "atm", "Pa") == 101325


def test_pressure_mmhg_to_pa():
    assert abs(convert(1, "mmHg", "Pa") - 133.322368) < 1e-6

def test_invalid_source_unit():
    with pytest.raises(ValueError):
        convert(5, "invalid", "Gy")

def test_invalid_target_unit():
    with pytest.raises(ValueError):
        convert(5, "Gy", "invalid")

def test_incompatible_dose_and_equivalent_dose():
    with pytest.raises(ValueError):
        convert(1, "Gy", "Sv")


def test_incompatible_energy_and_mass():
    with pytest.raises(ValueError):
        convert(1, "MeV", "kg")

def test_incompatible_radioactivity_and_dose():
    with pytest.raises(ValueError):
        convert(1, "Bq", "Gy")


def test_celsius_to_kelvin():
    assert convert(0, "°C", "K") == 273.15

def test_celsius_to_fahrenheit():
    assert convert(100, "°C", "°F") == 212

def test_fahrenheit_to_celsius():
    assert convert(32, "°F", "°C") == 0

def test_kelvin_to_celsius():
    assert convert(273.15, "K", "°C") == 0

def test_kelvin_to_fahrenheit():
    assert convert(273.15, "K", "°F") == 32
    
    
def test_gy_per_min_to_gy_per_s():
    assert round(convert(1, "Gy/min", "Gy/s"), 12) == round(1 / 60, 12)

def test_gy_per_h_to_gy_per_min():
    assert round(convert(1, "Gy/h", "Gy/min"), 12) == round(1 / 60, 12)

def test_mgy_per_h_to_gy_per_h():
    assert convert(1, "mGy/h", "Gy/h") == 0.001

def test_ugy_per_h_to_gy_per_h():
    assert convert(1, "μGy/h", "Gy/h") == 0.000001

def test_rad_per_s_to_gy_per_s():
    assert convert(1, "rad/s", "Gy/s") == 0.01

def test_rad_per_h_to_gy_per_h():
    assert convert(1, "rad/h", "Gy/h") == 0.01
    
def test_sv_per_min_to_sv_per_s():
    assert round(convert(1, "Sv/min", "Sv/s"), 12) == round(1 / 60, 12)

def test_sv_per_h_to_sv_per_min():
    assert round(convert(1, "Sv/h", "Sv/min"), 12) == round(1 / 60, 12)

def test_msv_per_h_to_sv_per_h():
    assert convert(1, "mSv/h", "Sv/h") == 0.001

def test_usv_per_h_to_sv_per_h():
    assert convert(1, "μSv/h", "Sv/h") == 0.000001

def test_rem_per_s_to_sv_per_s():
    assert convert(1, "rem/s", "Sv/s") == 0.01

def test_rem_per_h_to_sv_per_h():
    assert convert(1, "rem/h", "Sv/h") == 0.01
    
    
def test_m2_to_cm2():
    assert convert(1, "m²", "cm²") == 10000

def test_cm2_to_mm2():
    assert convert(1, "cm²", "mm²") == 100

def test_mm2_to_um2():
    assert convert(1, "mm²", "μm²") == 1000000

def test_cm2_to_m2():
    assert convert(10000, "cm²", "m²") == 1


def test_m3_to_l():
    assert convert(1, "m³", "L") == 1000

def test_l_to_ml():
    assert convert(1, "L", "mL") == 1000

def test_ml_to_ul():
    assert convert(1, "mL", "μL") == 1000

def test_cm3_to_ml():
    assert convert(1, "cm³", "mL") == 1

def test_mm3_to_ul():
    assert convert(1, "mm³", "μL") == 1

def test_l_to_cm3():
    assert convert(1, "L", "cm³") == 1000