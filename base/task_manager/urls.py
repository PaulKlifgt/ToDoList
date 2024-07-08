from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>', views.task, name='task'),
    path('add/', views.add, name='add'),
    path('complete/<int:task_id>', views.done, name='done'),
    path('uncomplete/<int:task_id>', views.undone, name='undone'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('change/<int:task_id>', views.change, name='change'),
]
