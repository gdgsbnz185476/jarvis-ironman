function setStatus(text) {
    document.getElementById("status").innerText = text;
}

function addMessage(sender, text) {
    let chat = document.getElementById("chat");
    chat.innerHTML += `<p><b>${sender}:</b> ${text}</p>`;
}

function updateBrain(text) {
    document.getElementById("brain").innerText = text;
}

function updateTasks(text) {
    document.getElementById("tasks").innerText = text;
}

function updateAuto(text) {
    document.getElementById("auto").innerText = text;
}

function updateMemory(text) {
    document.getElementById("memory").innerHTML += `<p>${text}</p>`;
}

async function send() {
    let input = document.getElementById("input").value;

    if (!input) return;

    setStatus("PROCESSING");

    addMessage("You", input);

    try {
        let res = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: input,
                speak_output: true
            })
        });

        let data = await res.json();

        addMessage("Jarvis", data.response);

        setStatus("IDLE");

    } catch (err) {
        setStatus("ERROR");
        addMessage("SYSTEM", err.toString());
    }

    document.getElementById("input").value = "";
}