"""User views."""

#Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.urls import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models

from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile


#Forms
from users.forms import  SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """user detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UserSignUpView(LoginRequiredMixin, FormView):
    """Users signup view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Update profile view"""
    template_name= 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number','picture']

    def get_object(self):
        """Return users profile"""
        return self.request.user.profile
    def get_success_url(self):
        """Return to users profile"""
        username = self.object.user.username
        return reverse_lazy('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """Login View."""

    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout View."""

    template_name = "users/login.html"






