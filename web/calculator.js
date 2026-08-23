const calculatorCards = document.querySelectorAll(".category-card");

const calculatorSections = document.querySelectorAll(".calculator-section");


/* =========================
   CALCULATOR NAVIGATION
   ========================= */

calculatorCards.forEach((card) => {

    card.addEventListener("click", () => {

        const calculator = card.dataset.calculator;

        const target = document.getElementById(calculator);

        if (target) {

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }

    });

});


/* =========================
   RADIOACTIVE DECAY
   ========================= */

const decayButton =
    document.getElementById("decayButton");


decayButton.addEventListener("click", () => {

    const initialActivity =
        Number(document.getElementById("initialActivity").value);

    const halfLife =
        Number(document.getElementById("halfLife").value);

    const decayTime =
        Number(document.getElementById("decayTime").value);


    if (
        !Number.isFinite(initialActivity) ||
        !Number.isFinite(halfLife) ||
        !Number.isFinite(decayTime) ||
        halfLife <= 0
    ) {

        document.getElementById("decayResult").textContent =
            "Please enter valid values.";

        return;
    }


    const remainingActivity =
        initialActivity *
        Math.pow(0.5, decayTime / halfLife);


    document.getElementById("decayResult").textContent =
        `${remainingActivity.toPrecision(8)}`;

});


/* =========================
   DOSE RATE
   ========================= */

const doseRateButton =
    document.getElementById("doseRateButton");


doseRateButton.addEventListener("click", () => {

    const dose =
        Number(document.getElementById("doseValue").value);

    const time =
        Number(document.getElementById("doseTime").value);


    if (
        !Number.isFinite(dose) ||
        !Number.isFinite(time) ||
        time <= 0
    ) {

        document.getElementById("doseRateResult").textContent =
            "Please enter valid values.";

        return;
    }


    const doseRate =
        dose / time;


    document.getElementById("doseRateResult").textContent =
        `${doseRate.toPrecision(8)}`;

});


/* =========================
   HVL / TVL
   ========================= */

const hvlButton =
    document.getElementById("hvlButton");


hvlButton.addEventListener("click", () => {

    const initialIntensity =
        Number(document.getElementById("initialIntensity").value);

    const layerNumber =
        Number(document.getElementById("layerNumber").value);

    const layerType =
        document.getElementById("layerType").value;


    if (
        !Number.isFinite(initialIntensity) ||
        !Number.isFinite(layerNumber) ||
        layerNumber < 0
    ) {

        document.getElementById("hvlResult").textContent =
            "Please enter valid values.";

        return;
    }


    let remainingIntensity;


    if (layerType === "HVL") {

        remainingIntensity =
            initialIntensity *
            Math.pow(0.5, layerNumber);

    } else {

        remainingIntensity =
            initialIntensity *
            Math.pow(0.1, layerNumber);

    }


    document.getElementById("hvlResult").textContent =
        `${remainingIntensity.toPrecision(8)}`;

});


/* =========================
   PERCENTAGE
   ========================= */

const percentageButton =
    document.getElementById("percentageButton");


percentageButton.addEventListener("click", () => {

    const value =
        Number(document.getElementById("percentageValue").value);

    const total =
        Number(document.getElementById("percentageTotal").value);


    if (
        !Number.isFinite(value) ||
        !Number.isFinite(total) ||
        total === 0
    ) {

        document.getElementById("percentageResult").textContent =
            "Please enter valid values.";

        return;
    }


    const percentage =
        (value / total) * 100;


    document.getElementById("percentageResult").textContent =
        `${percentage.toPrecision(8)} %`;

});


/* =========================
   DARK MODE
   ========================= */

const themeToggle =
    document.getElementById("themeToggle");


themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    const darkMode =
        document.body.classList.contains("dark-mode");


    themeToggle.textContent =
        darkMode ? "☀" : "☾";

});

/* =========================
   BACK TO MAIN PAGE
   ========================= */

const backToMain =
    document.getElementById("backToMain");


if (backToMain) {

    backToMain.addEventListener("click", () => {

        window.location.href = "index.html";

    });

}
