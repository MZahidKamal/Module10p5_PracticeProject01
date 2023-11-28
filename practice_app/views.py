from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    return render(request, 'practice_app/home.html')

def tasks(request):
    return render(request, 'practice_app/tasks.html')

def geeksforgeeks(request):
    data_dictionary = {
        'value1': "Practicing Django Filters",
        'value2': ['a', 'b', 'c', 'd', 'e', 'f'],
        'value3': 100,
        'value4': 'I\'m learning Django',
        'value5': 'django',
        'value6': 'Django',
        'value7': datetime.datetime.now(),
        'value8': '',
        'value9': [
            {'name': 'zed', 'age': 31},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 19},
        ],
        'value10': 100,
        'value11': "We know <  and  >  and  \'  and  \"  and  &",
        'value12': 123456789,
    }
    return render(request, 'practice_app/geeksforgeeks.html', context=data_dictionary)

def earthly(request):
    return render(request, 'practice_app/earthly.html')

def navigations(request):
    return render(request, 'practice_app/navigations.html')
































