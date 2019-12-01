from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=200, null=False)
    game_summary = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        photo_str = self.photo.url if self.photo else 'no photo'
        return f'{self.pk}: {self.game_name} {self.game_summary} {self.notes} {self.rating} {photo_str}'