const conversionFactors = {
    Gy: 1,
    rad: 0.01,

    Sv: 1,
    rem: 0.01,

    eV: 1,
    keV: 1e3,
    MeV: 1e6,
    GeV: 1e9
};


function convert(value, fromUnit, toUnit) {

    if (!(fromUnit in conversionFactors)) {
        throw new Error(`Unsupported source unit: ${fromUnit}`);
    }

    if (!(toUnit in conversionFactors)) {
        throw new Error(`Unsupported target unit: ${toUnit}`);
    }

    const baseValue = value * conversionFactors[fromUnit];

    return baseValue / conversionFactors[toUnit];
}


function formatResult(value) {

    if (Number.isInteger(value)) {
        return value.toString();
    }

    return Number(value.toPrecision(10)).toString();
}


document
    .getElementById("convertButton")
    .addEventListener("click", function () {

        const valueInput = document.getElementById("value");
        const fromUnit = document.getElementById("fromUnit").value;
        const toUnit = document.getElementById("toUnit").value;
        const resultElement = document.getElementById("result");

        const value = Number(valueInput.value);

        if (valueInput.value === "" || !Number.isFinite(value)) {

            resultElement.textContent = "Please enter a valid number.";

            return;
        }

        try {

            const result = convert(value, fromUnit, toUnit);

            resultElement.textContent =
                `${formatResult(result)} ${toUnit}`;

        } catch (error) {

            resultElement.textContent =
                error.message;
        }
    });
