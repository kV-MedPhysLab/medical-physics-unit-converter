const calculatorCards = document.querySelectorAll(".category-card");
calculatorCards.forEach((card) => {
    card.addEventListener("click", () => {
        const calculator = card.dataset.calculator;
        if (calculator === "radioactive-decay") {
            showRadioactiveDecay();
        }
        else if (calculator === "dose-rate") {
            showDoseRate();
        }
        else if (calculator === "hvl-tvl") {
            showHvlTvl();
        }
        else if (calculator === "percentage") {
            showPercentage();
        }
    });
});
function showRadioactiveDecay() {
    alert("Radioactive Decay Calculator — coming next.");
}
function showDoseRate() {
    alert("Dose Rate Calculator — coming next.");
}
function showHvlTvl() {
    alert("HVL / TVL Calculator — coming next.");
}
function showPercentage() {
    alert("Percentage Calculator — coming next.");
}