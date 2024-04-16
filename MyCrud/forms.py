from django.forms import ModelForm
from .models import UserAuth, BlogPost


class UserAuthForm(ModelForm):
    model = UserAuth
    fields = {'username', 'email', 'password'}


class BlogPostForm(ModelForm):
    model = BlogPost
    fields={'title', 'content', 'photo'}
