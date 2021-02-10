from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_activity = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user'


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_likes')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Like %s %s' % (self.user, self.post)

    class Meta:
        db_table = 'post_like'
        unique_together = (('user', 'post'),)
