from django.shortcuts import render
from django.db import models

# Create your views here.
def index1(request):
    return render(request, 'index.html')
    
def about1(request):
    return render(request, 'about.html')

def gallery1(request):
    return render(request, 'gallery.html')

def link1(request):
    return render(request, 'link.html')