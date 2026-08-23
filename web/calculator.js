const calculatorCards =
    document.querySelectorAll(".category-card");


calculatorCards.forEach((card) => {

    card.addEventListener("click", () => {

        const calculator =
            card.dataset.calculator;


        if (calculator === "radioactive-decay") {

            window.location.href =
                "calculators/radioactive-decay.html";

        }


        else if (calculator === "dose-rate") {

            window.location.href =
                "calculators/dose-rate.html";

        }


        else if (calculator === "hvl-tvl") {

            window.location.href =
                "calculators/hvl-tvl.html";

        }


        else if (calculator === "percentage") {

            window.location.href =
                "calculators/percentage.html";

        }

    });

});