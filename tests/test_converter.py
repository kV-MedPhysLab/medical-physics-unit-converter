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
