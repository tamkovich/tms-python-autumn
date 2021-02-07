from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"{self.title} - {self.content[:50]}"

    def __str__(self):
        return f"{self.title} - {self.content[:50]}"
