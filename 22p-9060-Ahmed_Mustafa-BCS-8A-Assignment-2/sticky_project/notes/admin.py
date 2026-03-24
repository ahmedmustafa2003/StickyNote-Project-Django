# Django admin panel ke liye imports
from django.contrib import admin
from .models import Note

# Note model ko admin panel mein register karana
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    # Admin list view mein kaunse fields dikhaney hain
    list_display = ('title', 'owner', 'pinned', 'created_at', 'color')
    # Filter karne ke options (sidebar mein)
    list_filter = ('created_at', 'owner', 'pinned')
    # Search box kaunse fields mein search kre
    search_fields = ('title', 'content')
    # Ye fields edit nahi ho sakte (read-only)
    readonly_fields = ('created_at', 'updated_at')
    # Form details ko organize karna
    fieldsets = (
        # Note ki details
        ('Note ke Details', {
            'fields': ('title', 'content', 'color')
        }),
        # Note ke options
        ('Options', {
            'fields': ('pinned',)
        }),
        # Metadata (uss taraf collapse hai)
        ('Metadata', {
            'fields': ('owner', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
