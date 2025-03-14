document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("https://your-backend-url.com/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "Erfolgreich eingeloggt!") {
            window.location.href = "/dashboard"; // Weiterleitung zu einem Dashboard
        } else {
            document.getElementById("error-message").innerText = data.message;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("error-message").innerText = "Es gab einen Fehler beim Login.";
    });
});
