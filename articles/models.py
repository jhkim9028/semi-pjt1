from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    unlike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unlike_articles')
    hitCount = models.IntegerField(default=0)
                            
class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,  related_name='recomment', null=True)
    text = models.TextField(blank=True)

class Popularsearch(models.Model):
    terms = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    searchCount = models.IntegerField(default=1)