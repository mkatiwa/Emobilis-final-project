from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='slide/')

    def __str__(self):
        return self.title


class Team(models.Model):
    position = models.CharField(max_length= 50)
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to ='teams/')
    twitter_url = models.CharField(max_length=60, blank = True)
    instagram_url = models.CharField(max_length=78, blank=True)
    facebook_url = models.CharField(max_length=78,blank=True)
    linkedin_url = models.CharField(max_length=78, blank=True)


def __str__(self):
    return self.name


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to ='board/', blank=False)
    twitter_url = models.CharField(max_length=60, blank = True)
    linkedin_url = models.CharField(max_length=78, blank=True)

def __str__(self):
    return self.description


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length= 150)
    logo = models.ImageField(max_length=45)

def __str__(self):
    return self.logo