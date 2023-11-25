from django.db import models

# Create your models here.

class Post(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=5)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.Name