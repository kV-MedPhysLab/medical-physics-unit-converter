const units = {

    radiation_dose: {
        "Gy": 1,
        "rad": 0.01
    },

    equivalent_dose: {
        "Sv": 1,
        "rem": 0.01
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
        "Ci": 3.7e10,
        "mCi": 3.7e7,
        "μCi": 3.7e4
    },

    length: {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "nm": 1e-9
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


function convert() {

    const value = Number(valueInput.value);

    if (valueInput.value === "" || !Number.isFinite(value)) {

        resultElement.textContent =
            "Please enter a valid number.";

        return;
    }


    const category = categorySelect.value;
    const categoryUnits = units[category];

    const fromUnit = fromUnitSelect.value;
    const toUnit = toUnitSelect.value;


    const baseValue =
        value * categoryUnits[fromUnit];

    const result =
        baseValue / categoryUnits[toUnit];


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
