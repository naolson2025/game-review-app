from django.db import models

class Review(models.Model):
    game_summary = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    rating = models.IntegerField()
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)