from django import forms
from .models import UserAuth, BlogPost


class UserAuthForm(forms.ModelForm):
    model = UserAuth
    fields = {'username', 'email', 'password'}


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields={'title', 'content', 'photo'}
