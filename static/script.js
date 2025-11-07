async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userText = input.value.trim();

  if (!userText) return;

  // Display user message
  const userMsg = document.createElement("div");
  userMsg.classList.add("user-message");
  userMsg.textContent = userText;
  chatBox.appendChild(userMsg);
  chatBox.scrollTop = chatBox.scrollHeight;

  input.value = "";

  // Send to backend (Flask)
  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: userText })
  });

  const data = await response.json();

  // Display bot response
  const botMsg = document.createElement("div");
  botMsg.classList.add("bot-message");
  botMsg.textContent = data.reply;
  chatBox.appendChild(botMsg);
  chatBox.scrollTop = chatBox.scrollHeight;
}
