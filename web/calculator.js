const calculatorCards =
    document.querySelectorAll(".category-card");

const calculatorSelection =
    document.getElementById("calculatorSelection");

const calculatorPanel =
    document.getElementById("calculatorPanel");

const calculatorTitle =
    document.getElementById("calculatorTitle");

const calculatorDescription =
    document.getElementById("calculatorDescription");

const backButton =
    document.getElementById("backToCalculators");


const calculators = {

    "radioactive-decay": {
        title: "Radioactive Decay",
        description:
            "Calculate remaining activity after radioactive decay.",
        element:
            document.getElementById("radioactiveDecayCalculator")
    },

    "dose-rate": {
        title: "Dose Rate",
        description:
            "Calculate dose rate using the inverse square law.",
        element:
            document.getElementById("doseRateCalculator")
    },

    "hvl-tvl": {
        title: "HVL / TVL",
        description:
            "Calculate total shielding thickness from HVLs.",
        element:
            document.getElementById("hvlTvlCalculator")
    },

    "percentage": {
        title: "Percentage Calculations",
        description:
            "Calculate a percentage from a value and a total.",
        element:
            document.getElementById("percentageCalculator")
    }

};


function hideAllCalculators() {

    Object.values(calculators).forEach((calculator) => {

        calculator.element.style.display = "none";

    });

}


function openCalculator(name) {

    const calculator = calculators[name];

    if (!calculator) {
        return;
    }

    hideAllCalculators();

    calculatorTitle.textContent =
        calculator.title;

    calculatorDescription.textContent =
        calculator.description;

    calculator.element.style.display =
        "block";

    calculatorSelection.style.display =
        "none";

    calculatorPanel.style.display =
        "block";

    window.scrollTo({
        top: calculatorPanel.offsetTop - 30,
        behavior: "smooth"
    });

}


calculatorCards.forEach((card) => {

    card.addEventListener("click", () => {

        const calculator =
            card.dataset.calculator;

        openCalculator(calculator);

    });

});


backButton.addEventListener("click", () => {

    calculatorPanel.style.display =
        "none";

    calculatorSelection.style.display =
        "block";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});


/* =========================
   RADIOACTIVE DECAY
   ========================= */

document
    .getElementById("calculateDecayButton")
    .addEventListener("click", () => {

        const initialActivity =
            Number(
                document.getElementById(
                    "initialActivity"
                ).value
            );

        const halfLife =
            Number(
                document.getElementById(
                    "halfLife"
                ).value
            );

        const time =
            Number(
                document.getElementById(
                    "decayTime"
                ).value
            );

        const result =
            document.getElementById(
                "decayResultValue"
            );


        if (
            !Number.isFinite(initialActivity) ||
            !Number.isFinite(halfLife) ||
            !Number.isFinite(time) ||
            initialActivity < 0 ||
            halfLife <= 0 ||
            time < 0
        ) {

            result.textContent =
                "Please enter valid values.";

            return;
        }


        const remainingActivity =
            initialActivity *
            Math.pow(
                2,
                -time / halfLife
            );


        result.textContent =
            `${Number(
                remainingActivity.toPrecision(10)
            )}`;

    });


/* =========================
   DOSE RATE
   ========================= */

document
    .getElementById("calculateDoseRateButton")
    .addEventListener("click", () => {

        const initialDoseRate =
            Number(
                document.getElementById(
                    "doseRateDistance"
                ).value
            );

        const initialDistance =
            Number(
                document.getElementById(
                    "initialDistance"
                ).value
            );

        const finalDistance =
            Number(
                document.getElementById(
                    "finalDistance"
                ).value
            );

        const result =
            document.getElementById(
                "doseRateResultValue"
            );


        if (
            !Number.isFinite(initialDoseRate) ||
            !Number.isFinite(initialDistance) ||
            !Number.isFinite(finalDistance) ||
            initialDoseRate < 0 ||
            initialDistance <= 0 ||
            finalDistance <= 0
        ) {

            result.textContent =
                "Please enter valid values.";

            return;
        }


        const finalDoseRate =
            initialDoseRate *
            Math.pow(
                initialDistance / finalDistance,
                2
            );


        result.textContent =
            `${Number(
                finalDoseRate.toPrecision(10)
            )}`;

    });


/* =========================
   HVL / TVL
   ========================= */

document
    .getElementById("calculateHvlButton")
    .addEventListener("click", () => {

        const hvl =
            Number(
                document.getElementById(
                    "hvlValue"
                ).value
            );

        const layers =
            Number(
                document.getElementById(
                    "tvlLayers"
                ).value
            );

        const result =
            document.getElementById(
                "hvlResultValue"
            );


        if (
            !Number.isFinite(hvl) ||
            !Number.isFinite(layers) ||
            hvl <= 0 ||
            layers < 0
        ) {

            result.textContent =
                "Please enter valid values.";

            return;
        }


        const totalThickness =
            hvl * layers;


        result.textContent =
            `${Number(
                totalThickness.toPrecision(10)
            )}`;

    });


/* =========================
   PERCENTAGE
   ========================= */

document
    .getElementById("calculatePercentageButton")
    .addEventListener("click", () => {

        const value =
            Number(
                document.getElementById(
                    "percentageValue"
                ).value
            );

        const total =
            Number(
                document.getElementById(
                    "percentageTotal"
                ).value
            );

        const result =
            document.getElementById(
                "percentageResultValue"
            );


        if (
            !Number.isFinite(value) ||
            !Number.isFinite(total) ||
            total === 0
        ) {

            result.textContent =
                "Please enter valid values.";

            return;
        }


        const percentage =
            (value / total) * 100;


        result.textContent =
            `${Number(
                percentage.toPrecision(10)
            )} %`;

    });


/* =========================
   DARK MODE
   ========================= */

const themeToggle =
    document.getElementById("themeToggle");


themeToggle.addEventListener(
    "click",
    () => {

        document.body.classList.toggle(
            "dark-mode"
        );

        const darkMode =
            document.body.classList.contains(
                "dark-mode"
            );

        themeToggle.textContent =
            darkMode ? "☀" : "☾";

    }
);