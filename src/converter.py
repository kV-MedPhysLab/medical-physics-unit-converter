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
    
    # Equivalent dose rate
    "Sv/s": ("equivalent_dose_rate", 1.0),
    "Sv/min": ("equivalent_dose_rate", 1 / 60),
    "Sv/h": ("equivalent_dose_rate", 1 / 3600),
    "mSv/h": ("equivalent_dose_rate", 1e-3 / 3600),
    "μSv/h": ("equivalent_dose_rate", 1e-6 / 3600),
    "rem/s": ("equivalent_dose_rate", 0.01),
    "rem/min": ("equivalent_dose_rate", 0.01 / 60),
    "rem/h": ("equivalent_dose_rate", 0.01 / 3600),

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
    "TBq": ("radioactivity", 1e12),
    "Ci": ("radioactivity", 3.7e10),
    "mCi": ("radioactivity", 3.7e7),
    "μCi": ("radioactivity", 3.7e4),

    # Length
    "m": ("length", 1.0),
    "cm": ("length", 1e-2),
    "mm": ("length", 1e-3),
    "μm": ("length", 1e-6),
    "nm": ("length", 1e-9),
    "Å": ("length", 1e-10),
    "pm": ("length", 1e-12),

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

    # Pressure
    "Pa": ("pressure", 1.0),
    "kPa": ("pressure", 1e3),
    "MPa": ("pressure", 1e6),
    "bar": ("pressure", 1e5),
    "atm": ("pressure", 101325.0),
    "mmHg": ("pressure", 133.322368),
    "psi": ("pressure", 6894.757293),

    # Temperature
    "°C": ("temperature", "celsius"),
    "K": ("temperature", "kelvin"),
    "°F": ("temperature", "fahrenheit"),
    
    # Radiation dose rate
    "Gy/s": ("radiation_dose_rate", 1.0),
    "Gy/min": ("radiation_dose_rate", 1 / 60),
    "Gy/h": ("radiation_dose_rate", 1 / 3600),
    "mGy/h": ("radiation_dose_rate", 1e-3 / 3600),
    "μGy/h": ("radiation_dose_rate", 1e-6 / 3600),
    "rad/s": ("radiation_dose_rate", 0.01),
    "rad/min": ("radiation_dose_rate", 0.01 / 60),
    "rad/h": ("radiation_dose_rate", 0.01 / 3600),
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

    # Temperature conversions require offsets
    if from_category == "temperature":

        # Convert source temperature to Celsius
        if from_unit == "°C":
            celsius = value

        elif from_unit == "K":
            celsius = value - 273.15

        elif from_unit == "°F":
            celsius = (value - 32) * 5 / 9

        # Convert Celsius to target temperature
        if to_unit == "°C":
            result = celsius

        elif to_unit == "K":
            result = celsius + 273.15

        elif to_unit == "°F":
            result = celsius * 9 / 5 + 32

        return round(result, 12)

    # Standard multiplicative conversions
    base_value = value * from_factor

    return round(base_value / to_factor, 12)