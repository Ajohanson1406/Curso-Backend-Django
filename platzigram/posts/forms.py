"""Posts forms."""

from django import forms
from posts.models import Post

# Create the form class.


class PostForm(forms.ModelForm):
    """Post model form"""
    class Meta:
        model =  Post
        fields = ['user', 'profile', 'title', 'photo']

