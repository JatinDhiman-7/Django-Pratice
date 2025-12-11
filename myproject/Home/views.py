from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable':'Raftaar is Great'
    }
    # messages.success(request,'This is a test message')
    return render(request,'index.html',context)
    # return HttpResponse('This is Home')
def about(request):
    return render (request,'about.html')

def services(request):
    return render (request,'services.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        # contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                date=datetime.today()
            )
        messages.success(request, "Your message has been sent")
    return render(request,'contact.html')