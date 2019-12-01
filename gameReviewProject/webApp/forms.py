from django import forms
from django.forms import FileInput
from .models import Review

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('game_name', 'game_summary', 'notes', 'rating', 'photo')