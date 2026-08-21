const units = {

    radiation_dose: {
        "Gy": 1,
        "rad": 0.01
    },

    radiation_dose_rate: {
        "Gy/s": 1,
        "Gy/min": 1 / 60,
        "Gy/h": 1 / 3600,
        "mGy/h": 1e-3 / 3600,
        "μGy/h": 1e-6 / 3600,
        "rad/s": 0.01,
        "rad/min": 0.01 / 60,
        "rad/h": 0.01 / 3600
    },

    equivalent_dose: {
        "Sv": 1,
        "rem": 0.01
    },

    equivalent_dose_rate: {
        "Sv/s": 1,
        "Sv/min": 1 / 60,
        "Sv/h": 1 / 3600,
        "mSv/h": 1e-3 / 3600,
        "μSv/h": 1e-6 / 3600,
        "rem/s": 0.01,
        "rem/min": 0.01 / 60,
        "rem/h": 0.01 / 3600
    },

    energy: {
        "eV": 1,
        "keV": 1e3,
        "MeV": 1e6,
        "GeV": 1e9
    },

    radioactivity: {
        "Bq": 1,
        "kBq": 1e3,
        "MBq": 1e6,
        "GBq": 1e9,
        "TBq": 1e12,
        "Ci": 3.7e10,
        "mCi": 3.7e7,
        "μCi": 3.7e4
    },

    length: {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "nm": 1e-9,
        "Å": 1e-10,
        "pm": 1e-12
    },

    mass: {
        "kg": 1,
        "g": 1e-3,
        "mg": 1e-6,
        "μg": 1e-9
    },

    time: {
        "s": 1,
        "ms": 1e-3,
        "μs": 1e-6,
        "min": 60,
        "h": 3600,
        "day": 86400
    },

    pressure: {
        "Pa": 1,
        "kPa": 1e3,
        "MPa": 1e6,
        "bar": 1e5,
        "atm": 101325,
        "mmHg": 133.322368,
        "psi": 6894.757293
    },

    temperature: {
        "°C": 1,
        "K": 1,
        "°F": 1
    }
};


const categorySelect = document.getElementById("category");
const valueInput = document.getElementById("value");
const fromUnitSelect = document.getElementById("fromUnit");
const toUnitSelect = document.getElementById("toUnit");
const convertButton = document.getElementById("convertButton");
const swapButton = document.getElementById("swapButton");
const resultElement = document.getElementById("result");


function populateUnits() {

    const category = categorySelect.value;
    const categoryUnits = units[category];

    fromUnitSelect.innerHTML = "";
    toUnitSelect.innerHTML = "";

    const unitNames = Object.keys(categoryUnits);

    unitNames.forEach((unit) => {

        const fromOption = document.createElement("option");
        fromOption.value = unit;
        fromOption.textContent = unit;

        fromUnitSelect.appendChild(fromOption);


        const toOption = document.createElement("option");
        toOption.value = unit;
        toOption.textContent = unit;

        toUnitSelect.appendChild(toOption);

    });


    if (unitNames.length > 1) {
        toUnitSelect.selectedIndex = 1;
    }
}


function formatResult(value) {

    if (value === 0) {
        return "0";
    }

    if (Math.abs(value) >= 1e-6 && Math.abs(value) < 1e9) {
        return Number(value.toPrecision(10)).toString();
    }

    return value.toExponential(6);
}


function convertTemperature(value, fromUnit, toUnit) {

    let celsius;

    if (fromUnit === "°C") {
        celsius = value;
    } else if (fromUnit === "K") {
        celsius = value - 273.15;
    } else if (fromUnit === "°F") {
        celsius = (value - 32) * 5 / 9;
    }

    if (toUnit === "°C") {
        return celsius;
    } else if (toUnit === "K") {
        return celsius + 273.15;
    } else if (toUnit === "°F") {
        return celsius * 9 / 5 + 32;
    }
}


function convert() {

    const value = Number(valueInput.value);

    if (valueInput.value === "" || !Number.isFinite(value)) {

        resultElement.textContent =
            "Please enter a valid number.";

        return;
    }


    const category = categorySelect.value;

    const fromUnit = fromUnitSelect.value;
    const toUnit = toUnitSelect.value;


    let result;

    if (category === "temperature") {

        result =
            convertTemperature(
                value,
                fromUnit,
                toUnit
            );

    } else {

        const categoryUnits = units[category];

        const baseValue =
            value * categoryUnits[fromUnit];

        result =
            baseValue / categoryUnits[toUnit];
    }


    resultElement.textContent =
        `${formatResult(result)} ${toUnit}`;
}


categorySelect.addEventListener(
    "change",
    populateUnits
);


convertButton.addEventListener(
    "click",
    convert
);


swapButton.addEventListener(
    "click",
    function () {

        const from =
            fromUnitSelect.value;

        const to =
            toUnitSelect.value;


        fromUnitSelect.value = to;
        toUnitSelect.value = from;


        if (valueInput.value !== "") {
            convert();
        }
    }
);


populateUnits();


const themeToggle =
    document.getElementById("themeToggle");


themeToggle.addEventListener(
    "click",
    function () {

        document.body.classList.toggle("dark-mode");

        const darkMode =
            document.body.classList.contains("dark-mode");

        themeToggle.textContent =
            darkMode ? "☀" : "☾";

    }
);