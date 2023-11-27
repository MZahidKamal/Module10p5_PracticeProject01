from django.shortcuts import render
from django.http import HttpResponse

import practice_app.urls


# Create your views here.
def home(request):
    return render(request, 'practice_app/home.html')

def tasks(request):
    return render(request, 'practice_app/tasks.html')

def geeksforgeeks(request):
    return render(request, 'practice_app/geeksforgeeks.html')

def earthly(request):
    return render(request, 'practice_app/earthly.html')

def navigations(request):
    return render(request, 'practice_app/navigations.html')
