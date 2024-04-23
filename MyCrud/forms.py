from django import forms
from .models import UserAuth, BlogPost, SearchItem, Upload

class UploadForm(forms.ModelForm):

    name = forms.TextInput()
    image = forms.ImageField()
    class Meta:
        model = Upload
        fields = ["name","image"]

class UserAuthForm(forms.ModelForm):
    model = UserAuth
    fields = {'username', 'email', 'password'}


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields={'title', 'content', 'photo'}


class SearchItemForm(forms.ModelForm):
    class Meta:
        model = SearchItem
        fields = '__all__'