"""
Medical Physics Unit Converter
==============================

Core unit conversion functions for common medical physics units.

Version: 0.2.0
Developed by kV-MedPhysLab.
"""

__version__ = "0.2.0"


UNITS = {

    # Radiation dose
    "Gy": ("radiation_dose", 1.0),
    "rad": ("radiation_dose", 0.01),

    # Equivalent dose
    "Sv": ("equivalent_dose", 1.0),
    "rem": ("equivalent_dose", 0.01),

    # Energy
    "eV": ("energy", 1.0),
    "keV": ("energy", 1e3),
    "MeV": ("energy", 1e6),
    "GeV": ("energy", 1e9),

    # Radioactivity
    "Bq": ("radioactivity", 1.0),
    "kBq": ("radioactivity", 1e3),
    "MBq": ("radioactivity", 1e6),
    "GBq": ("radioactivity", 1e9),
    "Ci": ("radioactivity", 3.7e10),
    "mCi": ("radioactivity", 3.7e7),
    "μCi": ("radioactivity", 3.7e4),

    # Length
    "m": ("length", 1.0),
    "cm": ("length", 1e-2),
    "mm": ("length", 1e-3),
    "μm": ("length", 1e-6),
    "nm": ("length", 1e-9),

    # Mass
    "kg": ("mass", 1.0),
    "g": ("mass", 1e-3),
    "mg": ("mass", 1e-6),
    "μg": ("mass", 1e-9),

    # Time
    "s": ("time", 1.0),
    "ms": ("time", 1e-3),
    "μs": ("time", 1e-6),
    "min": ("time", 60.0),
    "h": ("time", 3600.0),
    "day": ("time", 86400.0),
}


def convert(value, from_unit, to_unit):
    """
    Convert a numerical value between compatible units.

    Raises
    ------
    ValueError
        If either unit is unsupported or if the units belong
        to different physical quantities.
    """

    if from_unit not in UNITS:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    if to_unit not in UNITS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    from_category, from_factor = UNITS[from_unit]
    to_category, to_factor = UNITS[to_unit]

    if from_category != to_category:
        raise ValueError(
            f"Incompatible units: {from_unit} and {to_unit}"
        )

    base_value = value * from_factor

    return base_value / to_factor
