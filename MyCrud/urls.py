from django.urls import path
from .views import create_new_task, flickr, upload,blog
urlpatterns = [
    path('', create_new_task, name='create_new_task'),
    path('flickr/', flickr, name='flickr'),
    path('upload/', upload, name = 'upload'),
    path('blog/', blog, name='blog'),
    # path('sendmail/', send_email, name='send_email'),
    # path('send-email/', send_email_view, name='send_email'),
]
