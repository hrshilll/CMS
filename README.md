# Complaint Management System (CMS)

A full-featured Django web application for managing complaints in educational institutions. Supports multiple user roles (Admin, Faculty, Student) with role-based permissions, complete audit trails, file attachments, and a REST API.

## 🚀 Features

### Core Functionality
- **Multi-role System**: Admin, Faculty, and Student roles with different permissions
- **Complaint Management**: Create, assign, track, and resolve complaints
- **File Attachments**: Support for PDF, images, and documents (up to 10MB)
- **Status Tracking**: Pending → In Progress → Resolved → Closed workflow
- **Priority Management**: Low, Medium, High priority levels
- **Audit Trail**: Complete history of all complaint changes
- **Feedback System**: User feedback for resolved complaints
- **Auto-generated Complaint Numbers**: Format `CMP-YYYYMMDD-XXXXXX`

### Technical Features
- **REST API**: Django REST Framework with token authentication
- **Responsive UI**: Server-rendered Django templates with modern styling
- **File Security**: Safe file uploads with validation
- **Database**: SQLite for local development
- **Role-based Permissions**: Proper access control for all operations

## 📋 Requirements

- Python 3.11 or higher
- pip (Python package manager)
- SQLite (bundled with Python)

## 🛠️ Installation & Setup

### For macOS/Linux

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/CMS.git
cd CMS
```

#### 2. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables (Optional)
```bash
cp env.example .env
# Edit .env file if you want to customize settings
```

#### 5. Run Database Migrations
```bash
python manage.py migrate
```

#### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

#### 7. Load Sample Data (Optional)
```bash
python scripts/populate_sample_data.py
```

#### 8. Start Development Server
```bash
python manage.py runserver
```

Visit **http://localhost:8000** to access the application.

---

### For Windows

#### 1. Clone the Repository
```cmd
git clone https://github.com/yourusername/CMS.git
cd CMS
```

#### 2. Create Virtual Environment
```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### 3. Install Dependencies
```cmd
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables (Optional)
```cmd
copy env.example .env
:: Edit .env file if you want to customize settings
```

#### 5. Run Database Migrations
```cmd
python manage.py migrate
```

#### 6. Create Superuser (Admin)
```cmd
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

#### 7. Load Sample Data (Optional)
```cmd
python scripts\populate_sample_data.py
```

#### 8. Start Development Server
```cmd
python manage.py runserver
```

Visit **http://localhost:8000** to access the application.

## 🔧 Common Commands

### Development
```bash
# Start development server
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Open Django shell
python manage.py shell
```

### Database
```bash
# Reset database (WARNING: Deletes all data)
rm db.sqlite3
python manage.py migrate

# Export data
python manage.py dumpdata > backup.json

# Import data
python manage.py loaddata backup.json
```

## 📁 Project Structure

```
CMS/
├── config/                 # Django configuration
│   ├── settings.py        # Main settings file
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── complaints/            # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── serializers.py     # API serializers
│   ├── forms.py           # Django forms
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin interface
│   └── templates/         # HTML templates
├── templates/             # Global templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded files
├── scripts/               # Utility scripts
├── fixtures/              # Sample data
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── env.example            # Environment variables template
└── README.md              # This file
```
