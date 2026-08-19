"""
Medical Physics Unit Converter
==============================

Core unit conversion functions for common medical physics units.

Version: 0.1.0
Developed by kV-MedPhysLab.
"""


__version__ = "0.1.0"


# Conversion factors to a common base unit
CONVERSION_FACTORS = {
    # Dose
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
}


def convert(value, from_unit, to_unit):
    """
    Convert a numerical value from one unit to another.

    Parameters
    ----------
    value : float
        Numerical value to convert.
    from_unit : str
        Unit of the input value.
    to_unit : str
        Desired output unit.

    Returns
    -------
    float
        Converted value.

    Raises
    ------
    ValueError
        If either unit is not supported.
    """

    if from_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported source unit: {from_unit}")

    if to_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    # Convert to the common base unit
    base_value = value * CONVERSION_FACTORS[from_unit]

    # Convert from the base unit to the target unit
    result = base_value / CONVERSION_FACTORS[to_unit]

    return result
