from django.db import models

# Create your models here.

class audio_file(models.Model):
    device_id = models.CharField(max_length=100)
    audio_file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)




