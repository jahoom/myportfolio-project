from django.db import models

class Job(models.Model):
    """docstring for ."""
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
