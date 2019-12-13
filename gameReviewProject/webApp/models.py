from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=200, null=False)
    game_summary = models.TextField(blank=True, null=False)
    reviewers_opinion = models.TextField(blank=True, null=False)
    # Found validators on stack overflow
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)], null=False)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)
    video_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        photo_str = self.photo if self.photo else 'no photo'
        return f'{self.pk}: {self.game_name} {self.game_summary} {self.reviewers_opinion} {self.rating} {photo_str} {self.video_id}'


# This model is used to get the user's search and implement the search
class Search(models.Model):
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    video_search = models.CharField(max_length=200, null=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.video_search}'