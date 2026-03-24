"""
Django ke main project ke URLs.
Yeh file tanam URLs ko routes karti hai Views tak.

Sticky Notes App ke tamam URLs:
- /admin/ - Django admin panel
- / - Notes app ke tamam URLs (register, login, notes, etc.)
"""

# Django imports
from django.contrib import admin
from django.urls import path, include

# Main URL patterns
urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),
    # Notes app ke tamam URLs yahan include karo
    path('', include('notes.urls')),
]
