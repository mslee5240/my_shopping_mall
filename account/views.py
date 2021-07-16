from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request, 'account/home.html')

def user_login(request):
    if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)

        if user is not None : 
            login(request, user)
            return redirect('home')
        else : 
            return render(request, 'account/login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다. '})
    else : 
        return render(request, 'account/login.html')

def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"], 
                university = request.POST["university"],
                profile_image = request.FILES.get('profile_image')
            )
            user.save()
            auth.login(request, user)
            return redirect('home')
        else : 
            return render(request, 'account/signup.html')
    else: 
        return render(request, 'account/signup.html')

def user_logout(request) : 
    logout(request)
    return redirect('home')