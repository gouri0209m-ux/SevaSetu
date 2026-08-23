# SevaSetu – NGO Management System

SevaSetu is a web-based NGO Management System built with Django and Bootstrap. It provides a simple platform for managing NGO campaigns, volunteers, donations and community contact activities.

## Features

- User registration, login and logout
- Campaign listing and campaign details
- Volunteer applications
- Donation records
- Contact message management
- Dashboard with project statistics
- Django admin panel
- Demo data through a custom `seed_data` command
- Responsive Bootstrap-based interface

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite
- **Version Control:** Git, GitHub

## Project Structure

```text
SevaSetu/
├── accounts/        # Authentication
├── campaigns/       # Campaigns and demo data
├── core/            # Main pages and dashboard
├── engagement/      # Volunteers, donations and contact messages
├── config/          # Django project settings and URLs
├── static/          # CSS, JavaScript and images
├── templates/       # Shared templates
├── manage.py
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gouri0209m-ux/SevaSetu.git
cd SevaSetu
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Add demo data

```bash
python manage.py seed_data
```

This creates sample campaigns, volunteer applications and donations for demonstration.

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Main Pages

- `/` – Home
- `/about/` – About SevaSetu
- `/campaigns/` – Campaigns
- `/gallery/` – Gallery
- `/volunteer/` – Volunteer application
- `/donate/` – Donation form
- `/contact/` – Contact form
- `/accounts/register/` – Registration
- `/accounts/login/` – Login
- `/dashboard/` – Dashboard
- `/admin/` – Django administration

## Database Modules

### Campaign
Stores campaign title, description, image, location, target amount, dates and status.

### Volunteer Application
Stores volunteer name, email, phone, skills and selected campaign.

### Donation
Stores donor name, email, campaign and amount.

### Contact Message
Stores name, email, subject and message.

## Future Scope

- Online payment gateway
- Email notifications
- User profiles
- Campaign progress tracking
- Report generation
- More detailed analytics

## Academic Project

**Project:** SevaSetu – NGO Management System  
**Framework:** Django  
**Database:** SQLite  
**Purpose:** Academic and educational use

## Author

**Gouri Mishra**  
GitHub: https://github.com/gouri0209m-ux
