# microblog/models.py
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title