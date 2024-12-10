// Add a subtle fade-in effect when the document is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".container");
    container.classList.add("animate__animated", "animate__fadeIn");

    // Load stored data into the form on page load
    const form = document.querySelector("form");
    if (form) {
        const inputs = form.querySelectorAll("input, select");
        inputs.forEach((input) => {
            const savedValue = localStorage.getItem(input.name);
            if (savedValue !== null) {
                input.value = savedValue;
            }
        });
    }
});

// Store input data in local storage on change
const form = document.querySelector("form");
if (form) {
    const inputs = form.querySelectorAll("input, select");
    inputs.forEach((input) => {
        input.addEventListener("change", function () {
            localStorage.setItem(input.name, input.value);
        });
    });
}

// Example function to simulate button click animation
const button = document.querySelector(".button");
if (button) {
    button.addEventListener("click", function () {
        button.classList.add("animate__animated", "animate__pulse");
    });
}


