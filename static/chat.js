// static/chat.js

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('message');
  const chat = document.getElementById('chat');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;

    appendMessage('user', message);
    input.value = '';

    console.log('Submitting message:', message); // ✅ check this in console

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }

      const data = await response.json();
      appendMessage('bot', data.reply || '[No response]');
    } catch (err) {
      appendMessage('bot', `Error: ${err.message}`);
    }
  });

  function appendMessage(sender, text) {
    const div = document.createElement('div');
    div.className = `bubble ${sender}`;
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }
});
