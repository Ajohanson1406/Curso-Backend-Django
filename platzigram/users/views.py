"""User views."""

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exeption
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile


def login_view(request):
    username = request.POST.get('username', True)
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('feed')
        
    else:
        return render(request, 'users/login.html', {'error': 'Invalid username and password'})


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()
        login(request, user)
        return redirect('feed')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
     """logout users."""
     logout(request)
     return redirect('login')