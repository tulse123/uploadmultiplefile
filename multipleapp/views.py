import imp
from django.shortcuts import render
from . models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def upload(request):
    if request.method == 'POST':
        images=request.FILES.getlist('images')
        for img in images:
            photo=Photo.objects.create(image=img)
            photo.save()
        return HttpResponseRedirect('/')
    else:
        return  HttpResponse("not avv")




