from django.db import models

class Blog(models.Model):
    """docstring for ."""
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
