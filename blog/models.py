from typing import Optional
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pinned = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")
    
