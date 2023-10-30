from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Siz allaqachon tizimga kirib bolgansiz!")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return HttpResponse("Username yoki parol not`g`ri ")
    return render(request, "users/login.html")

@login_required(login_url="login")
def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        has_error = False
        if User.objects.filter(email=email):
            messages.error(request, "Ushbu email bilan foydalanuvchi mavjud.")
            has_error = True
        if User.objects.filter(username=username):
            messages.error(request, "Bu username bilan foydalanuvchi mavjud.")
            has_error = True
        if password1 != password2:
            messages.error(request, "Parollar o`aro bir xil emas.")
            has_error = True
        if len(password1) < 8:
            messages.error(request, "parol kamida 8 ta belgidan iborat bo`lishi kerak ")
            has_error = True

        if not has_error:
            user = User.objects.create(email=email, username=username, first_name=first_name)
            user.set_password(password1)
            user.save()
            return redirect('login')
        else:
            pass
    return render(request, "users/signup.html") 


