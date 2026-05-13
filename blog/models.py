from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    image = models.ImageField(
        upload_to='post_images/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # Like System
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username