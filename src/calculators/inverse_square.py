"""
Inverse square law calculations for radiation physics.

Developed by kV-MedPhysLab.
"""


def calculate_inverse_square(initial_value, initial_distance, new_distance):
    """
    Calculate radiation intensity or dose rate at a new distance.

    Parameters
    ----------
    initial_value : float
        Initial intensity or dose rate.
    initial_distance : float
        Initial distance from the source.
    new_distance : float
        New distance from the source.

    Returns
    -------
    float
        Intensity or dose rate at the new distance.

    Notes
    -----
    The two distances must use the same unit.

    Formula
    -------
    I2 = I1 * (r1 / r2)^2
    """

    if initial_value < 0:
        raise ValueError("Initial value must be non-negative.")

    if initial_distance <= 0:
        raise ValueError("Initial distance must be greater than zero.")

    if new_distance <= 0:
        raise ValueError("New distance must be greater than zero.")

    return initial_value * (initial_distance / new_distance) ** 2