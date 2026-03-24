from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Note
from .forms import NoteForm, RegisterForm

# ============ Daraksh ke liye Views / Authentication Views ============

def register_view(request):
    """Naye users apne account register Karen."""
    # Agar user pehle se logged in hai to notes page par bhej do
    if request.user.is_authenticated:
        return redirect('notes:note_list')
    
    # Jab user form submit kare
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Naya user banao aur save karo
            user = form.save()
            messages.success(request, 'Account banaya gaya! Ab login Karen.')
            return redirect('notes:login')
        else:
            # Form mein errors ho to dikha do
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


# Login ka custom view
class CustomLoginView(LoginView):
    """Django ka built-in LoginView custom settings ke saath."""
    # Login template
    template_name = 'login.html'
    # Agar user pehle se logged in hai to login page mein na rakhna
    redirect_authenticated_user = True
    # Login ke baad notes page par bhej do
    success_url = reverse_lazy('notes:note_list')


# Logout ka custom view
class CustomLogoutView(LogoutView):
    """Django ka built-in LogoutView custom settings ke saath."""
    # Logout ke baad login page par bhej do
    next_page = reverse_lazy('notes:login')


# ============ Notes ke Views (Login zaroori) / @login_required ============

# Taman notes ko display karny wala view
@login_required(login_url='notes:login')
def note_list(request):
    """Logged-in user ke tamen notes dikha do search aur pagination ke saath."""
    # Sirf us user ke notes nikalo joh logged in hai
    notes = Note.objects.filter(owner=request.user)
    # Search query GET parameters mein se nikalna
    search_query = request.GET.get('search', '').strip()
    
    # Agar user search kre to title ya content mein search kro
    if search_query:
        notes = notes.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
    
    # Total notes ka count
    total_notes = notes.count()
    
    # Pagination - 10 notes per page
    paginator = Paginator(notes, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Context mein data dal do jise template use karey
    context = {
        'page_obj': page_obj,
        'notes': page_obj.object_list,
        'total_notes': total_notes,
        'search_query': search_query,
        'has_search': bool(search_query),
        'paginator': paginator,
    }
    return render(request, 'note_list.html', context)


# Naya note banane ka view
@login_required(login_url='notes:login')
def note_create(request):
    """Naya note banao aur save karo."""
    # Jab user form submit kre
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            # Form se data nikalo par abhi save na kro
            note = form.save(commit=False)
            # Note ka malik yeh user set kro
            note.owner = request.user
            # Ab note database mein save kro
            note.save()
            messages.success(request, f'Note "{note.title}" banaya gaya!')
            return redirect('notes:note_list')
    else:
        # Naya empty form dikha do
        form = NoteForm()
    
    # Form ko template mein bhej do
    context = {'form': form, 'action': 'Create'}
    return render(request, 'note_form.html', context)


# Mosajuda note ko edit karne ka view
@login_required(login_url='notes:login')
def note_edit(request, pk):
    """Mosajuda note ko edit karo."""
    # Note ko ID se nikalo ya error dikha do
    note = get_object_or_404(Note, pk=pk)
    
    # Check karo ke kya yeh note logged-in user ka hai
    if note.owner != request.user:
        messages.error(request, 'Aap kisi aur ke note ko edit nahi kar sakte.')
        return redirect('notes:note_list')
    
    # Jab user form submit kre
    if request.method == 'POST':
        # Existing note ke saath form ko fill kro
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # Note ko update karke save kro
            form.save()
            messages.success(request, f'Note "{note.title}" update hua!')
            return redirect('notes:note_list')
    else:
        # Existing note ke data se form pre-fill kro
        form = NoteForm(instance=note)
    
    context = {'form': form, 'action': 'Edit', 'note': note}
    return render(request, 'note_form.html', context)


# Note ko delete karne ka view
@login_required(login_url='notes:login')
def note_delete(request, pk):
    """Note ko delete karo confirmation ke saath."""
    # Note ko ID se nikalo
    note = get_object_or_404(Note, pk=pk)
    
    # Check karo ke kya yeh note logged-in user ka hai
    if note.owner != request.user:
        messages.error(request, 'Aap kisi aur ke note ko delete nahi kar sakte.')
        return redirect('notes:note_list')
    
    # Jab user delete confirm kre
    if request.method == 'POST':
        # Note ka title save kro message ke liye
        note_title = note.title
        # Note ko delete kro
        note.delete()
        messages.success(request, f'Note "{note_title}" delete ho gaya!')
        return redirect('notes:note_list')
    
    # Delete confirmation template mein context bhej do
    context = {'note': note}
    return render(request, 'note_confirm_delete.html', context)
