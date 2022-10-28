from django.contrib import admin
from .models import Meme

# Register models for testing (mockup data) on admin page
admin.site.register(Meme)