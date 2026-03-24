# 📝 Sticky Notes App

A clean, functional web app for creating, editing, and managing sticky notes with Django.

## Features

✨ **Core Features:**
- 🔐 User authentication (Register, Login, Logout)
- 📝 Create, Read, Update, Delete (CRUD) notes
- 🎨 Color-coded sticky notes (pick any color)
- 📌 Pin important notes to the top
- 🔍 Search notes by title or content
- 📄 Paginated note list (10 notes per page)
- 📊 Real-time character counter while typing
- 🔒 Secure - Users can only see/edit their own notes

## Technology Stack

- **Backend:** Django 4.2+
- **Database:** SQLite (default, configurable)
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Python:** 3.8+

## Installation & Setup

### 1. Clone or Navigate to Project

```bash
cd /Users/ahmedmustafamughal/Desktop/Web-Technology-Assignment-2
```

### 2. Install Dependencies

```bash
pip3 install django
```

### 3. Apply Database Migrations

```bash
python3 manage.py migrate
```

### 4. Create a Superuser (Optional - for Django Admin)

```bash
python3 manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Run the Development Server

```bash
python3 manage.py runserver
```

The app will be available at: **http://127.0.0.1:8000/**

## Project Structure

```
Web-Technology-Assignment-2/
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database
├── README.md                          # This file
│
├── sticky_project/                    # Project configuration
│   ├── settings.py                    # Main settings
│   ├── urls.py                        # Main URL router
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│
└── notes/                             # Main app
    ├── models.py                      # Note model definition
    ├── views.py                       # View logic
    ├── forms.py                       # Django forms
    ├── urls.py                        # App URL routes
    ├── admin.py                       # Django admin configuration
    ├── migrations/                    # Database migrations
    │   ├── 0001_initial.py
    │   └── 0002_alter_note_options_note_pinned.py
    │
    └── templates/                     # HTML templates
        ├── base.html                  # Base template (navbar, layout)
        ├── note_list.html             # Display all notes
        ├── note_form.html             # Create/edit note form
        ├── note_confirm_delete.html   # Delete confirmation
        ├── register.html              # User registration
        └── login.html                 # User login
```

## URL Routes

### Authentication
- `/register/` - Create a new account
- `/login/` - Sign in to your account
- `/logout/` - Sign out

### Notes
- `/notes/` - View all your notes (with search & pagination)
- `/notes/new/` - Create a new note
- `/notes/<id>/edit/` - Edit an existing note
- `/notes/<id>/delete/` - Delete a note (with confirmation)

### Admin (Optional)
- `/admin/` - Django admin panel (create superuser first)

## Usage Guide

### Creating a Note
1. Click **"+ New Note"** in the navigation bar
2. Enter a title and content
3. Pick a color from the color picker
4. Optionally check **"📌 Pin this note"** to pin it
5. Click **"✨ Create Note"**

### Searching Notes
1. Use the search bar on the **My Notes** page
2. Search by note title or content (case-insensitive)
3. Results update instantly
4. Click **"Clear"** to reset the search

### Editing a Note
1. Click **"Edit"** on any note card
2. Modify title, content, color, or pin status
3. Click **"💾 Update Note"**

### Deleting a Note
1. Click **"Delete"** on any note card
2. Review the note details on the confirmation page
3. Click **"🗑️ Delete Permanently"** to confirm

### Pinning Notes
- Check the **"📌 Pin this note"** checkbox when creating or editing
- Pinned notes appear at the top with a 📌 icon
- Uncheck to unpin

### Pagination
- Note list shows 10 notes per page
- Use pagination buttons to navigate
- Search terms are preserved when navigating pages

## Character Counter

The note content field includes a live character counter:
- **Gray text** (normal): 0-2,500 characters
- **Orange text** (warning): 2,500-3,500 characters
- **Red text** (danger): 3,500+ characters

## Development Commands

```bash
# Run the development server
python3 manage.py runserver

# Create migrations for model changes
python3 manage.py makemigrations

# Apply migrations to the database
python3 manage.py migrate

# Open Django shell for testing
python3 manage.py shell

# View admin panel (requires superuser)
# Visit: http://127.0.0.1:8000/admin/

# Create a superuser for admin access
python3 manage.py createsuperuser
```

## Database

By default, the app uses **SQLite** (`db.sqlite3`), which is perfect for development.

To use a different database (PostgreSQL, MySQL), update `DATABASES` in `sticky_project/settings.py`.

## Security Notes

✅ **What's Protected:**
- Passwords are hashed using Django's security system
- CSRF protection on all forms
- Users can only access/edit their own notes
- Session-based authentication
- HTTP-only cookies for secure sessions

⚠️ **For Production:**
- Set `DEBUG = False` in settings.py
- Configure `ALLOWED_HOSTS` with your domain
- Use environment variables for `SECRET_KEY`
- Set up HTTPS/SSL
- Use a production database (PostgreSQL recommended)
- Use a production server (Gunicorn, Waitress)

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python3 manage.py runserver 8001
```

### Database Errors
Reset the database and migrations:
```bash
rm db.sqlite3
python3 manage.py migrate
```

### Django Not Found
Install Django:
```bash
pip3 install django
```

### Import Errors
Ensure you're in the correct directory:
```bash
cd /Users/ahmedmustafamughal/Desktop/Web-Technology-Assignment-2
```

## Future Enhancements

Ideas for expanding the app:
- 📧 Email notifications
- 🏷️ Tags/categories for notes
- 🔔 Note reminders/alarms
- 🤝 Share notes with other users
- 📱 Mobile app version
- 🌙 Dark mode
- 🎵 Voice notes
- 📎 File attachments

## License

This project is free to use and modify.

## Support

For issues or questions, ensure:
1. Django is installed: `pip3 install django`
2. Migrations are applied: `python3 manage.py migrate`
3. You're in the correct directory
4. Python 3.8+ is installed: `python3 --version`

---

**Happy note-taking!** 📝✨
