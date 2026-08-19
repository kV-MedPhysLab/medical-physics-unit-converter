"""
Tests for the Medical Physics Unit Converter.
"""

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


def test_same_unit():
    assert convert(5, "Gy", "Gy") == 5


def test_invalid_source_unit():
    try:
        convert(5, "invalid", "Gy")
        assert False
    except ValueError:
        assert True


def test_invalid_target_unit():
    try:
        convert(5, "Gy", "invalid")
        assert False
    except ValueError:
        assert True
