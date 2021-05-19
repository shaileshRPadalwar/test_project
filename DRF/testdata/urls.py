from django.urls import include, path
from .views import *
 
urlpatterns = [
    path('create-task/', task_list.as_view()),
]