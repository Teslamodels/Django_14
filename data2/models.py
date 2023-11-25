from django.db import models

# Create your models here.


class B(models.Model):
    Title = models.CharField(max_length=100)
    Text = models.TextField()
    
    def __str__(self):
        return self.Title