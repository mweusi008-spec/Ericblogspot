# Ericblogspot

A Django-based real-time news and forex blog with live market data, RSS-powered news feeds, and an admin-managed emergency alert system.

## Features

- **AI News** — auto-updated from TechCrunch AI RSS feed
- **Cybersecurity News** — auto-updated from The Hacker News RSS feed
- **Forex News** — live exchange rates, gold price, and forex news from ForexLive
- **Emergency News** — admin-created urgent alerts with a scrolling ribbon banner
- **Contact Page** — email, WhatsApp, and Telegram links managed from admin
- **Auto-refresh** — pages update every 30–60 seconds without reload
- **Admin Panel** — add/edit news, manage emergency alerts, update contact info
- **Responsive Design** — mobile-friendly light theme with Bootstrap 5

## Tech Stack

- **Backend:** Django 6.0.7
- **Frontend:** Bootstrap 5, custom CSS
- **Database:** SQLite (local), PostgreSQL (production)
- **Hosting:** Configured for Render
- **APIs:** Exchange Rate API, Gold API, RSS feeds

## Local Setup

```powershell
# Clone repo
git clone https://github.com/mweusi008-spec/Ericblogspot.git
cd Ericblogspot

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run dev server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and admin at `http://127.0.0.1:8000/admin/`

## Deployment

This project is configured for **Render** free tier:

1. Push to GitHub
2. Create PostgreSQL database on Render (free plan)
3. Create Web Service with:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn config.wsgi:application --log-file -`
   - Env vars: `DATABASE_URL`, `SECRET_KEY`, `DEBUG=false`, `DJANGO_SETTINGS_MODULE=config.settings`, `PYTHON_VERSION=3.11.0`
4. After deploy, visit `/setup-admin/` to create admin user
5. Site will be live at `https://ericblogspot.onrender.com`

## Admin Usage

- Add news via **News** section
- Set **Category** to `Emergency` and check **Is emergency** for urgent alerts
- Emergency news appears as a scrolling red ribbon on all pages
- Update contact details via **Contact Info** section
- Delete emergency news to remove the ribbon

## Project Structure

```
core/                 - Main app (views, models, URLs, context processors)
news/                 - News app (registered in admin)
templates/            - HTML templates
static/css/           - Custom stylesheets
config/               - Django settings and WSGI config
requirements.txt      - Python dependencies
Procfile              - Render start command
render.yaml           - Render deployment config
build.sh              - Build script for Render
```

## License

Private project — all rights reserved.
