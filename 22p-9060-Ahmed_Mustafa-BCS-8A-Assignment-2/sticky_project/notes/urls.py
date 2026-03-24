# URLs ko handle karne ke liye imports
from django.urls import path
from . import views

# App ka namespace - reverse() functions mein use hoga
app_name = 'notes'

# URL patterns - routes define karna
urlpatterns = [
    # ===== Daraksh ke URLs (Authentication) =====
    path('register/', views.register_view, name='register'),           # Naya account
    path('login/', views.CustomLoginView.as_view(), name='login'),     # Login
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Logout
    
    # ===== Notes ke URLs (CRUD operations) =====
    path('notes/', views.note_list, name='note_list'),                 # Taman notes
    path('notes/new/', views.note_create, name='note_create'),         # Naya note
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),   # Note edit
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),  # Note delete
]
