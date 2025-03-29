# README.md for Aithena

# Aithena 🧠

Aithena is an AI-driven Django web application designed to explore intelligent features, automation, and powerful backend capabilities.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment (`venv`)
- Django 5.x

### Setup

1. Clone the repository (if applicable)
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash# Aithena 🧠

   ```

Aithena is a full-stack AI-powered chatbot web application built with Django and OpenAI's GPT API. It features a clean UI, a typed chat interface, Tailwind CSS styling, and full Docker-based development and deployment.

Live at 👉 https://aithena.onrender.com

---

## 🚀 Features

- 🤖 Chatbot powered by OpenAI's `gpt-3.5-turbo`
- 💬 Web UI with Tailwind CSS and animated chat bubbles
- ⚙️ REST API endpoint for AI responses (`/api/chat`)
- 📦 Docker-based development and production
- 🌐 Deployed on [Render](https://render.com)
- ✅ WhiteNoise static file handling
- 🧪 Unit testing + test coverage with `coverage`

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.1
- Tailwind CSS (via CDN for now)
- OpenAI SDK (v1+)
- Gunicorn
- Docker + Docker Compose
- Render for deployment

---

## 🔧 Local Development

```bash
git clone https://github.com/nic-thompson/aithena.git
cd aithena
docker compose up --build
```

Access at [http://localhost:8000](http://localhost:8000)

---

## 📂 Project Structure

```
aithena/
├── chat/                # Chat app with views, urls, templates
├── core/                # Future core logic
├── static/              # chat.js and other assets
├── templates/           # chat.html (UI)
├── Dockerfile           # Container build
├── docker-compose.yml   # Dev environment
├── requirements.txt     # Python dependencies
└── manage.py
```

---

## 🔑 Environment Variables

Create a `.env` file (locally or in Render):

```env
OPENAI_API_KEY=sk-...
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=aithena.onrender.com,localhost,127.0.0.1
DEBUG=False
```

---

## 🧪 Running Tests

```bash
docker compose exec web coverage run manage.py test
```

View report:

```bash
coverage report
```

---

## 💬 API Usage

- `POST /api/chat`

```json
{
  "message": "Hello, Aithena!"
}
```

Response:

```json
{
  "reply": "Hi there! How can I help you today?"
}
```

---

## 🎯 Roadmap

- [x] Chat UI with streaming
- [x] Tailwind CSS polish
- [x] Dockerize and deploy to Render
- [ ] Add support for image/file upload
- [ ] Add persistent chat history
- [ ] OAuth login

---

## 🧠 Made by Nicolas Thompson

Chat with purpose. Built with care.

python manage.py migrate

````
5. Start the development server:
```bash
python manage.py runserver
````

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 🧩 Project Structure

```
aithena/
├── manage.py
├── core/            # Core app (home view, routes)
├── aithena/         # Project settings and URL routing
├── venv/            # Virtual environment (excluded from Git)
└── README.md
```

---

## 🛠️ Features

- Django 5.x backend
- JSON-based API views
- Modular structure for future AI capabilities

---

## 🧹 Local Dev Tips

- Use `.env` for secrets (add it to `.gitignore`)
- Keep virtual environment isolated
- Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages

---

## 📜 License

MIT – Use it freely and make something amazing.
