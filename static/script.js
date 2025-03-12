document.addEventListener("DOMContentLoaded", loadFeedback);

function submitFeedback() {
    let name = document.getElementById("name").value;
    let message = document.getElementById("message").value;

    if (name === "" || message === "") {
        alert("Mohon isi nama dan feedback!");
        return;
    }

    fetch("/submit_feedback", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, message })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadFeedback();
    });

    document.getElementById("name").value = "";
    document.getElementById("message").value = "";
}

function loadFeedback() {
    fetch("/get_feedback")
        .then(response => response.json())
        .then(feedbackList => {
            let feedbackContainer = document.getElementById("feedback-list");
            feedbackContainer.innerHTML = "";

            feedbackList.forEach(feedback => {
                let listItem = document.createElement("li");
                listItem.textContent = `${feedback.name}: ${feedback.message}`;
                feedbackContainer.appendChild(listItem);
            });
        });
}
