# microblog/serializers.py
from rest_framework import serializers
from .models import Tag, Post

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'tags', 'scheduled_time']
        read_only_fields =["author"]
