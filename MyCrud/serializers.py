from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import BlogPost



class BlogModel:
    def __init__(self, title,content):
        self.tite = title
        self.content = content



class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = BlogModel('Hello world', 'klsdjflksjlkdjklsd')
    model_sr = BlogSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().model(model_sr.data)
    print(json)

