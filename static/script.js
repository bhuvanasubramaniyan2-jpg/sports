const input = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");
const chatBox = document.getElementById("chat-box");

function addMessage(text, type) {
    const message = document.createElement("div");
    message.className = `message ${type}`;

    const icon = document.createElement("span");
    icon.textContent = type === "user" ? "👤" : "🤖";

    const p = document.createElement("p");
    p.textContent = text;

    message.appendChild(icon);
    message.appendChild(p);
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        addMessage(data.reply || "Sorry, something went wrong.", "bot");
    } catch (error) {
        addMessage("Unable to connect to the server.", "bot");
    }
}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
