document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript loaded successfully!");
    const button = document.querySelector("button");
    button.addEventListener("mouseover", () => {
        button.style.backgroundColor = "#0056b3";
    });
    button.addEventListener("mouseout", () => {
        button.style.backgroundColor = "#007bff";
    });
});
