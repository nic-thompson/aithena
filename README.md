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
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

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
