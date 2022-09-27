from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone

# Create your models here.

# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pinned = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True)



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")

    class Meta:
        ordering = ['-pub_date']
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
