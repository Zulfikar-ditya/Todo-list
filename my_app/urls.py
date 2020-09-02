from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add'),
    path('my_todo/', views.my_todo, name='my_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete'),
    path('you_are_logged_in/', views.you_are_loged_in, name='logged_in'),
]