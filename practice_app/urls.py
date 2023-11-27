from django.urls import path
from .views import home, tasks, geeksforgeeks, earthly, navigations

urlpatterns = [
    path('', home),
    path('home/', home),
    path('tasks/', tasks),
    path('geeksforgeeks/', geeksforgeeks),
    path('earthly/', earthly),
    path('navigations/', navigations),
]
