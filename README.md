# Gym Tracker

A simple app that lets you track which days you went to the gym. You get an interactive calendar: **click a day to mark it as a gym day**, click again to unmark it.

## What you need

- **Python 3** (e.g. 3.10 or 3.11). Check with: `python3 --version`

## How to run the app

All commands below are run from the **`backend`** folder (where `manage.py` lives).

### 1. Open the project folder in a terminal

```bash
cd /Users/sam/Desktop/gym-tracker/backend
```

### 2. (Optional) Create a virtual environment

This keeps the project’s packages separate from the rest of your system:

```bash
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
```

### 3. Install Django

```bash
pip install django
```

### 4. Create the database tables

Django needs to create the tables for gym visits:

```bash
python manage.py migrate
```

### 5. Create a user account

You need at least one user to log in:

```bash
python manage.py createsuperuser
```

Enter a username, email (optional), and password when asked.

### 6. Start the server

```bash
python manage.py runserver
```

### 7. Open the app in your browser

- **Calendar:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
  (You’ll be redirected to log in if you aren’t already.)
- **Admin (optional):** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) — log in with your superuser to see all gym visits.

## How to use the calendar

- **Log in** with the username and password you created.
- Use **Prev / Next** to change the month.
- **Click a day** to mark it as “I went to the gym.” Click again to remove the mark.
- The purple highlight shows gym days; the counter shows how many times you went that month.

## Project structure (for learning)

- **`backend/`** – Django project
  - **`api/`** – app that handles gym visits
    - **`models.py`** – defines `GymVisit` (user + date)
    - **`views.py`** – calendar page and “toggle visit” logic
    - **`templates/calendar.html`** – the calendar page and its styling/script
  - **`backend/`** – Django settings and main URLs
  - **`templates/registration/login.html`** – login page

## Stopping the server

In the terminal where the server is running, press **Ctrl+C**.

---

Enjoy tracking your gym days.
