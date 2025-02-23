from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def postfile(instance, filename):
    return os.path.join('feed/media/', instance.catagory, filename)

class Post(models.Model):
    CATAGORY =(
        ('Web Developement', 'Web Development'),
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Computer Science', 'Computer Science'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Health', 'Health'),
        ('Others', 'Others')

    )
    title= models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    catagory = models.CharField(max_length=100, choices=CATAGORY, null=True, blank= True)
    img = models.ImageField(upload_to=postfile,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # FIXED typo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
