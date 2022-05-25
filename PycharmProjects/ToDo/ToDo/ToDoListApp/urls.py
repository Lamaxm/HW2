from django.urls import path
import ToDo.ToDoListApp.views

urlpatterns = [
    path('',ToDo.ToDoListApp.views.home , name ='home'),
    path('', ToDo.ToDoListApp.about,name='about')
]