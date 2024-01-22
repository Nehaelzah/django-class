from django.db import models
from django.contrib.auth.models import User

BLOG_STATUS=

# Create your models here.
class Todo(models.Model):
    todo=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    done=models.BooleanField(default=False)
    def __str__(self):
        return self.todo
class Blog(models.Model):
    title=models.CharField(max_length=15),
    description=models.TextField(help_text="Enter a description"),
    status=models.CharField(max_length=2,choices=BLOG_STATUS),
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name="blog_likes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    