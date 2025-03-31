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

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });

      if (!response.ok) throw new Error(`HTTP error ${response.status}`);

      const data = await response.json();
      appendMessage('bot', data.reply || '[No response]');
    } catch (err) {
      appendMessage('bot', `Error: ${err.message}`);
    }
  });

  function appendMessage(sender, text) {
    const div = document.createElement('div');

    const baseStyle = 'px-4 py-2 max-w-[75%] rounded-lg inline-block';
    const userStyle = 'bg-blue-100 self-end ml-auto text-right';
    const botStyle = 'bg-green-100 self-start mr-auto text-left';

    div.className = `flex ${
      sender === 'user' ? userStyle : botStyle
    } ${baseStyle}`;
    div.textContent = text;

    const wrapper = document.createElement('div');
    wrapper.className = 'flex';
    wrapper.appendChild(div);

    chat.appendChild(wrapper);
    chat.scrollTop = chat.scrollHeight;
  }
});
