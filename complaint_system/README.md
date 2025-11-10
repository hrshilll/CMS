# Complaint Management System (CMS)

Simple local-only Django app. No Docker, no external services. Run with `python manage.py runserver`.

## 🚀 Features

### Core Functionality
- **Multi-role System**: Admin, Faculty, and Student roles with different permissions
- **Complaint Management**: Create, assign, track, and resolve complaints
- **File Attachments**: Support for PDF, images, and documents (up to 10MB)
- **Status Tracking**: Pending → In Progress → Resolved → Closed workflow
- **Priority Management**: Low, Medium, High priority levels
- **Audit Trail**: Complete history of all complaint changes
- **Feedback System**: User feedback for resolved complaints

### Technical Features
- **REST API**: Django REST Framework
- **UI**: Server-rendered Django templates
- **File Security**: Safe file uploads with validation
- **Database**: SQLite (local)

## 📋 Requirements

- Python 3.11+
- SQLite (bundled)

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/complaint-management-system.git
   cd complaint-management-system
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` to access the application.

## 🔧 Configuration

### Notes
- Uses SQLite locally; no other services required.

## 👥 User Roles

### Admin
- Manage all complaints
- Assign complaints to faculty
- Close complaints
- Access admin panel
- Export reports
- Manage users and categories

### Faculty
- View assigned complaints
- Update complaint status
- Add remarks
- Cannot close complaints

### Student
- Create complaints
- View own complaints
- Add feedback for resolved complaints
- Cannot edit complaints after submission

## 🔌 API Documentation

### Authentication
```bash
# Get authentication token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

### Complaints API

#### List Complaints
```bash
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/complaints/
```

#### Create Complaint
```bash
curl -X POST http://localhost:8000/api/complaints/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Network Issue",
    "description": "Internet connectivity problems",
    "category": 1,
    "priority": "HIGH"
  }'
```

#### Update Complaint Status
```bash
curl -X PATCH http://localhost:8000/api/complaints/CMP-20241201-000001/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status": "IN_PROGRESS"}'
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/complaints/` | List complaints |
| POST | `/api/complaints/` | Create complaint |
| GET | `/api/complaints/{id}/` | Get complaint details |
| PATCH | `/api/complaints/{id}/` | Update complaint |
| POST | `/api/complaints/{id}/assign/` | Assign complaint |
| GET | `/api/categories/` | List categories |
| GET | `/api/subcategories/` | List subcategories |
| GET | `/api/stats/` | Get statistics |
| POST | `/api/export/` | Export complaints |

## 🧪 Optional (Tests)
If you have pytest installed, you can run tests with `pytest`.

## 📊 Logging
Basic console logging enabled for development.

## 🔒 Security Features

- **Authentication**: Django's built-in authentication
- **Authorization**: Role-based permissions
- **CSRF Protection**: Enabled for all forms
- **XSS Prevention**: Template auto-escaping
- **SQL Injection**: ORM-based queries
- **File Upload Security**: Type and size validation
- **Rate Limiting**: API and login rate limits
- **Security Headers**: Comprehensive security headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation
- Use meaningful commit messages

## 📝 License
MIT

## 🆘 Support

- **Documentation**: [Wiki](https://github.com/yourusername/complaint-management-system/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/complaint-management-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/complaint-management-system/discussions)

## 🗺️ Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced reporting dashboard
- [ ] Integration with external systems
- [ ] Multi-language support
- [ ] Advanced workflow customization
- [ ] Real-time chat support

## 🙏 Acknowledgments

- Django community for the excellent framework
- Tailwind CSS for the utility-first CSS framework
- All contributors and users of this project

---

**Made with ❤️**
