from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    location = models.FileField(upload_to='files/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.location.delete()
        super().delete(*args, **kwargs)
        
