# Databases aur Models ke liye imports
from django.db import models
from django.contrib.auth.models import User

# Note Model - Sticky notes ke data structure ka blueprint
class Note(models.Model):
    # Note ke title ka field (maximum 200 characters)
    title = models.CharField(max_length=200)
    
    # Note ke content/mawad ka field (lamba text)
    content = models.TextField()
    
    # Note ke rang ka field (hex color code, default yellow)
    color = models.CharField(max_length=7, default='#FFFF99')
    
    # Note kab banaya gya ye tarikh (khud ba khud set ho jati hai)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Note kab update hua ye tarikh (har dafaa update hone par change hoti hai)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Note ka malik/owner - Django ke User model se connection
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Agar note important hai to pin Karen (True/False)
    pinned = models.BooleanField(default=False)

    # Jab Note ko string mein display Karen to title dikhe
    def __str__(self):
        return self.title

    # Database mein notes ki tarteeb (pehle pinned, phir newest)
    class Meta:
        ordering = ['-pinned', '-created_at']
