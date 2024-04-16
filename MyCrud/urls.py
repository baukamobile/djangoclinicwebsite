from django.urls import path
from .views import showPost
urlpatterns = [
    path('', showPost, name='show')
]
