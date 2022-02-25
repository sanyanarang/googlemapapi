from multiprocessing import context
from tkinter import E
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def index(request):
    if request.method == "GET":
        ob = Contact.objects.all()
        return render(request, 'index.html',{"value":ob})
    elif request.method=="POST":
        contact=Contact()
        name= request.POST.get('name')
        password= request.POST.get('password')
        email= request.POST.get('email')
        mobile= request.POST.get('mobile')
        id= request.POST.get('id')
        latitude= request.POST.get('latitude')
        longitude= request.POST.get('longitude')
        contact.name=name
        contact.password=password
        contact.email=email
        contact.mobile=mobile
        contact.id=id
        contact.latitude=latitude
        contact.longitude=longitude
        contact.save()  
        return HttpResponseRedirect("/show")
 
def show(request):
    ob =  Contact.objects.all()
    return render(request,"contact.html",{"value":ob})


def map(request):
    return render(request,"map.html")
       