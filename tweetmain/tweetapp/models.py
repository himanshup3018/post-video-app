from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="photos/",blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/',validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    # thumbnail = models.ImageField(upload_to='thumnails/',validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpg'])])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.description[:10]}'