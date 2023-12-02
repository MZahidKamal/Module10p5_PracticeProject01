from django.urls import path
from .views import home, tasks, geeksforgeeks, earthly, navigations

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('geeksforgeeks/', geeksforgeeks, name='geeksforgeeks'),
    path('earthly/', earthly, name='earthly'),
    path('navigations/', navigations, name='navigations'),
]
