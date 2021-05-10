import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Board_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user}"


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    author_name = models.ForeignKey(
        "Board_User", related_name="articles", on_delete=models.CASCADE, null=True
    )
    # up_votes = models.ManyToManyField(User)
    amount_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Post by {self.author_name}; Upvotes ={self.amount_of_upvotes}"


class Comment(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Article", related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Comment by {self.author_name}, on post: {self.post}"
