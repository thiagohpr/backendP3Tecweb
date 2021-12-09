from django.db import models

class Lista (models.Model):
    title = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=3,decimal_places=1)
    state = models.TextField()
    url = models.TextField(default='')