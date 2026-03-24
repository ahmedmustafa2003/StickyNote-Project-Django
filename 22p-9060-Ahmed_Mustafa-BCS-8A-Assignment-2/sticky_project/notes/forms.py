# Forms ke liye Django imports
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Note

# Note banane ya edit karne ke liye form
class NoteForm(forms.ModelForm):
    """Form jisse naye notes banate hain ya purane notes ko edit karte hain."""
    
    class Meta:
        model = Note
        # Jo fields user ko dikhaenge form mein
        fields = ['title', 'content', 'color', 'pinned']
        # Form fields ko styling aur features dena
        widgets = {
            # Title input field
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apna note ka naam likhen',
                'maxlength': 200,
            }),
            # Content textarea field
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Apna note likhen',
                'rows': 8,
                'id': 'contentField',
            }),
            # Color picker field
            'color': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control',
                'style': 'height: 50px;',
            }),
            # Pin checkbox field
            'pinned': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


# Naya account banane ke liye form
class RegisterForm(UserCreationForm):
    """Form jisse naye users apna account register karte hain."""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        # Registration form ke fields
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            # Username field
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Aik unique username chunein',
            }),
            # Email field
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apna email likhen',
            }),
        }
    
    # Password fields ko styling dena
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Password 1
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password likhen'
        # Password 2 (confirmation)
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password dobara likhen'
