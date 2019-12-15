from django.db import models

class Blog(models.Model):
    """docstring for ."""
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        zwrotka = ""
        if len(self.text)>100:
            zwrotka = self.text[:100]+'...'
        else:
            zwrotka = self.text
        return zwrotka

    def date_text(self):
        return str(self.date)[:-14]
