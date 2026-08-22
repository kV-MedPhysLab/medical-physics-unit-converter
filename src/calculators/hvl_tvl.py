"""
HVL and TVL calculations for radiation shielding.

Developed by kV-MedPhysLab.
"""

import math


def calculate_after_layers(initial_value, layers, layer_type="HVL"):
    """
    Calculate radiation intensity after a given number of HVLs or TVLs.

    Parameters
    ----------
    initial_value : float
        Initial radiation intensity or dose rate.
    layers : float
        Number of HVLs or TVLs.
    layer_type : str
        "HVL" or "TVL".

    Returns
    -------
    float
        Radiation intensity or dose rate after attenuation.
    """

    if initial_value < 0:
        raise ValueError("Initial value must be non-negative.")

    if layers < 0:
        raise ValueError("Number of layers must be non-negative.")

    layer_type = layer_type.upper()

    if layer_type == "HVL":
        transmission = 0.5 ** layers
    elif layer_type == "TVL":
        transmission = 0.1 ** layers
    else:
        raise ValueError("Layer type must be 'HVL' or 'TVL'.")

    return initial_value * transmission


def calculate_layers(initial_value, final_value, layer_type="HVL"):
    """
    Calculate the number of HVLs or TVLs required to reduce
    an initial value to a target final value.

    Parameters
    ----------
    initial_value : float
        Initial radiation intensity or dose rate.
    final_value : float
        Target radiation intensity or dose rate.
    layer_type : str
        "HVL" or "TVL".

    Returns
    -------
    float
        Required number of HVLs or TVLs.
    """

    if initial_value <= 0:
        raise ValueError("Initial value must be greater than zero.")

    if final_value <= 0:
        raise ValueError("Final value must be greater than zero.")

    if final_value > initial_value:
        raise ValueError(
            "Final value cannot be greater than initial value."
        )

    layer_type = layer_type.upper()

    if layer_type == "HVL":
        attenuation_factor = 0.5
    elif layer_type == "TVL":
        attenuation_factor = 0.1
    else:
        raise ValueError("Layer type must be 'HVL' or 'TVL'.")

    return math.log(final_value / initial_value) / math.log(
        attenuation_factor
    )