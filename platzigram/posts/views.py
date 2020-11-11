"""posts views."""

#Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

#Models
from posts.models import Post

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return a Detail view of a post"""
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg ='post_id'
    queryset = Post.objects.all()


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publish posts"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to user"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

   