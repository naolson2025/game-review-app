from django import forms
from django.forms import FileInput, ValidationError
from .models import Review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('game_name', 'game_summary', 'reviewers_opinion', 'rating', 'photo')

    # Clean the rating input from the user so they only enter a number 1 - 10
    def clean_rating(self):
        # set rating variable to the user's input
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 10:
            raise ValidationError('Please enter a rating 1-10')

        return rating