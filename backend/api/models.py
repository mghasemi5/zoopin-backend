from django.db import models
from django.utils.text import slugify

class Partner(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    tagline = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='partners/', blank=True, null=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    link = models.CharField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
class InfoBlock(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='info_icons/')
    description = models.TextField()

    def __str__(self):
        return self.title

class logos(models.Model):
    icon = models.ImageField(upload_to='logos/')
    description = models.TextField()


    def __str__(self):
        return self.icon

class insights(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='insights/', blank=True, null=True)
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to='insights_file/', blank=True, null=True)



    def __str__(self):
        return self.title

class testimonials(models.Model):

    qoute = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class slider(models.Model):

    image = models.ImageField(upload_to='slider/', blank=True, null=True)
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption