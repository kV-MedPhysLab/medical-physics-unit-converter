# Medical Physics Unit Converter

A lightweight scientific unit conversion tool for medical physics, radiation physics, and biomedical research.

## Current Version

**v0.1.0**

## Supported Conversions

### Radiation Dose

- Gy ↔ rad

### Equivalent Dose

- Sv ↔ rem

### Energy

- eV ↔ keV
- eV ↔ MeV
- eV ↔ GeV
- keV ↔ MeV
- keV ↔ GeV
- MeV ↔ GeV

## Usage

The converter can be used directly from Python.

```python
from converter import convert

result = convert(5, "Gy", "rad")

print(result)

Validation

Automated tests are run using pytest.

Tests are automatically executed through GitHub Actions whenever changes are pushed to the main branch.

Development Status

This project is currently under active development.

Future versions may include:

Radioactivity conversions
Length conversions
Mass conversions
Time conversions
Additional medical physics units
Web-based interface
About

Developed by kV-MedPhysLab.

Founded by Konstantinos Vasilopoulos.

Disclaimer

This tool is intended for educational, research, and non-clinical purposes.

It is not intended to replace validated clinical, regulatory, or commercial software.

License

License information will be added in a future release.
