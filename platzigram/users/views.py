"""User views."""

#Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('feed')
        
    else:
        return render(request, 'users/login.html', {'error': 'Invalid username and password'})