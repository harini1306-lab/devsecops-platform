console.log("DevSecOps Platform loaded successfully");

document.addEventListener("DOMContentLoaded", () => {
    console.log("Pipeline dashboard is ready");
    loadPipelineStatus();
});

async function loadPipelineStatus() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/status");

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const pipeline = await response.json();

        console.log("Pipeline data received:", pipeline);

        pipeline.forEach(item => {
            console.log(`${item.stage}: ${item.status}`);

            const cards = document.querySelectorAll(".cards .card");

            cards.forEach(card => {
                const title = card.querySelector("h3");

                if (title && title.textContent.trim() === item.stage) {
                    const statusElement = card.querySelector(".success");

                    if (statusElement) {
                        statusElement.textContent = item.status;
                    }
                }
            });
        });

    } catch (error) {
        console.error("Failed to connect to backend:", error);
    }
}