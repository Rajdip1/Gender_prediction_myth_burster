const form = document.getElementById("gender-form");
const resultEl = document.getElementById("result");
const submitBtn = document.getElementById("submit-btn");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    submitBtn.textContent = "Predicting...";
    submitBtn.disabled = true;

    const formData = new FormData(form);

    const payload = {
        mother_age: Number(formData.get("mother_age")),
        delivery_week: Number(formData.get("delivery_week")),
        health_score: Number(formData.get("health_score")),
        stress_level: Number(formData.get("stress_level")),
        work_hours: Number(formData.get("work_hours")),
        sleep_hours: Number(formData.get("sleep_hours")),
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        const data = await response.json();
        const gender = data.predicted_gender;

        resultEl.className = "result " + (gender === "Girl" ? "girl" : "boy");
        resultEl.textContent = `🍼 Result: ${gender}`;

    } catch (err) {
        resultEl.textContent = "❌ Server error";
        resultEl.style.color = "red";
    }

    submitBtn.textContent = "Predict";
    submitBtn.disabled = false;
});
