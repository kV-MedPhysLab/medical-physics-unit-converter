"""
Comparison calculations for medical physics.

Developed by kV-MedPhysLab.
"""


def calculate_percentage_difference(value_1, value_2):
    """
    Calculate the percentage difference between two values.

    Formula
    -------
    Percentage difference =
        |value_1 - value_2| / ((value_1 + value_2) / 2) * 100

    Parameters
    ----------
    value_1 : float
        First value.
    value_2 : float
        Second value.

    Returns
    -------
    float
        Percentage difference.
    """

    if value_1 < 0 or value_2 < 0:
        raise ValueError("Values must be non-negative.")

    if value_1 == 0 and value_2 == 0:
        return 0.0

    mean_value = (value_1 + value_2) / 2

    return abs(value_1 - value_2) / mean_value * 100