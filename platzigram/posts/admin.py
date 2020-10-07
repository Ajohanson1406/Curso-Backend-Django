"""post application module."""

from django.contrib import admin
from django.apps import AppConfig

# Register your models here.

class PostsConfig(AppConfig):
    """Posts application settings."""
    
    name="posts"
    varbose_name = "Posts"
