from django.shortcuts import render
from home.models import User
from django.contrib.auth import aauthenticate
# from django import auth
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        User.objects.create(
            name=name,
            email=email,
        )
    return render(request,'register.html')
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        user=aauthenticate(name=name,email=email)
        return render(request,'welcome.html')
def logout(request):
    return render(request,'logout.html')
