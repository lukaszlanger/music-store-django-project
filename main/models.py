# main/models.py

from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.album.title}"
