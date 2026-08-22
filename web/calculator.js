const calculatorCards = document.querySelectorAll(".category-card");

calculatorCards.forEach((card) => {

    card.addEventListener("click", () => {

        const calculator = card.dataset.calculator;

        if (calculator === "radioactive-decay") {
            window.location.href = "calculators/radioactive-decay.html";
        }

    });

});