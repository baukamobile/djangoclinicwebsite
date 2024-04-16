from django.urls import path
from .views import create_new_task
urlpatterns = [
    path('', create_new_task, name='create_new_task')
]
