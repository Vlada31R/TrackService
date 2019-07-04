from django import forms
from .models import *
from django.core.exceptions import ValidationError


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_data(self):
        new_genre = self.cleaned_data['title'].lower()

        if new_genre == 'create':
            raise ValidationError('Genre can not be "Create"')
        if Genre.objects.filter(slug__iexact=new_genre).count():
            raise ValidationError('Genre "{}" has already created'.format(new_genre))
        return new_genre


class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = ['title', 'performer', 'genres']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'performer': forms.TextInput(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
