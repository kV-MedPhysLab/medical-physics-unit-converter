"""
Medical Physics Unit Converter
==============================

Core unit conversion functions for common medical physics units.

Version: 0.2.0
Developed by kV-MedPhysLab.
"""

__version__ = "0.2.0"


CONVERSION_FACTORS = {

    # Radiation dose
    "Gy": 1.0,
    "rad": 0.01,

    # Equivalent dose
    "Sv": 1.0,
    "rem": 0.01,

    # Energy
    "eV": 1.0,
    "keV": 1e3,
    "MeV": 1e6,
    "GeV": 1e9,

    # Radioactivity
    "Bq": 1.0,
    "kBq": 1e3,
    "MBq": 1e6,
    "GBq": 1e9,
    "Ci": 3.7e10,
    "mCi": 3.7e7,
    "μCi": 3.7e4,

    # Length
    "m": 1.0,
    "cm": 1e-2,
    "mm": 1e-3,
    "μm": 1e-6,
    "nm": 1e-9,

    # Mass
    "kg": 1.0,
    "g": 1e-3,
    "mg": 1e-6,
    "μg": 1e-9,

    # Time
    "s": 1.0,
    "ms": 1e-3,
    "μs": 1e-6,
    "min": 60.0,
    "h": 3600.0,
    "day": 86400.0,
}


def convert(value, from_unit, to_unit):
    """
    Convert a numerical value from one unit to another.
    """

    if from_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    if to_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    base_value = value * CONVERSION_FACTORS[from_unit]

    result = base_value / CONVERSION_FACTORS[to_unit]

    return result
