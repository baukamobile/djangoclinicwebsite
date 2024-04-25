from django.urls import path
from django.views.generic import TemplateView
from .views import create_new_task, showPage,upload,blog, send_email_view
urlpatterns = [
    # path('', create_new_task, name='create_new_task'),
    path('', showPage, name='showpage'),
    path('upload/', upload, name = 'upload'),
    path('blog/', blog, name='blog'),
    path("index/", TemplateView.as_view(template_name="clinic-website-template/index.html"), name='index'),
    path('about/', TemplateView.as_view(template_name='clinic-website-template/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='clinic-website-template/contact.html'), name='contact'),
    path('service/', TemplateView.as_view(template_name='clinic-website-template/service.html'), name='service'),
    path('team/', TemplateView.as_view(template_name='clinic-website-template/team.html'), name='team'),
    path('feature/', TemplateView.as_view(template_name='clinic-website-template/feature.html'), name='feature'),
    path('appointment/', TemplateView.as_view(template_name='clinic-website-template/appointment.html'), name='appointment'),
    path('testimonial/', TemplateView.as_view(template_name='clinic-website-template/testimonial.html'), name='testimonial'),
    path('404/', TemplateView.as_view(template_name='clinic-website-template/404.html'), name='404'),
    path('auth/',create_new_task, name='create_new_task' ),
    path('sendmail/', send_email_view, name='send_email'),
    # path('send-email/', send_email_view, name='send_email'),
]
