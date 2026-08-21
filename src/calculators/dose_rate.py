"""
Dose, dose rate, and irradiation time calculations.

Developed by kV-MedPhysLab.
"""


def calculate_dose(dose_rate, time):
    """
    Calculate absorbed dose from dose rate and time.

    Parameters
    ----------
    dose_rate : float
        Dose rate in Gy/s.
    time : float
        Irradiation time in seconds.

    Returns
    -------
    float
        Absorbed dose in Gy.
    """

    if dose_rate < 0 or time < 0:
        raise ValueError("Dose rate and time must be non-negative.")

    return dose_rate * time


def calculate_dose_rate(dose, time):
    """
    Calculate dose rate from absorbed dose and time.

    Parameters
    ----------
    dose : float
        Absorbed dose in Gy.
    time : float
        Irradiation time in seconds.

    Returns
    -------
    float
        Dose rate in Gy/s.
    """

    if dose < 0 or time < 0:
        raise ValueError("Dose and time must be non-negative.")

    if time == 0:
        raise ValueError("Time must be greater than zero.")

    return dose / time


def calculate_time(dose, dose_rate):
    """
    Calculate irradiation time from absorbed dose and dose rate.

    Parameters
    ----------
    dose : float
        Absorbed dose in Gy.
    dose_rate : float
        Dose rate in Gy/s.

    Returns
    -------
    float
        Irradiation time in seconds.
    """

    if dose < 0 or dose_rate < 0:
        raise ValueError("Dose and dose rate must be non-negative.")

    if dose_rate == 0:
        raise ValueError("Dose rate must be greater than zero.")

    return dose / dose_rate