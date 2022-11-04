from django.db import models
from django.conf import settings

# Create your models here.
class ServiceCenter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='service_photos', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reverse_service")
    
class ServiceComment(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE, related_name='center')
    created_at = models.DateTimeField(auto_now_add=True)