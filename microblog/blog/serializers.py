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

    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')  # change
    #     post = Post.objects.create(**validated_data)  # change
    #
    #     for tag_data in tags_data:
    #         Tag.objects.create(post=post, **tag_data)  # change
    #     return post
    #
    # def update(self, instance, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     tags = (instance.tags).all()
    #     tags = list(tags)
    #
    #     super().update(instance, validated_data)
    #
    #     for tag_data in tags_data:
    #         tag = tags.pop(0)
    #         tag.name = tag_data.get('name', tag.name)
    #         tag.save()
    #     return instance