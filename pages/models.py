from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    degination = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class My_Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    degination = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
