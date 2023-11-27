from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is home page.')

def tasks(request):
    return HttpResponse('This is problem_tasks page.')

def geeksforgeeks(request):
    return HttpResponse('This is template_filters_from_geeksforgeeks page.')

def earthly(request):
    return HttpResponse('This is template_filters_from_earthly page.')

def navigations(request):
    return HttpResponse('This is page_navigations page.')
