const messages = document.getElementById("messages");
const form = document.getElementById("form");
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

// textContent, not innerHTML: neither the user nor the model must be able to inject HTML.
function show(text, type) {
  const bubble = document.createElement("div");
  bubble.className = `message ${type}`;
  bubble.textContent = text;
  messages.append(bubble);
  messages.scrollTop = messages.scrollHeight;
}

async function requestResponse(message) {
  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  const data = await response.json();
  if (typeof data.response !== "string" || !data.response.trim()) {
    throw new Error("Respuesta sin texto");
  }
  return data.response;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  show(message, "user");
  input.value = "";
  sendButton.disabled = true;

  try {
    show(await requestResponse(message), "bot");
  } catch (error) {
    console.error(error);
    show("No he podido obtener una respuesta. Inténtalo de nuevo.", "error");
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
});
