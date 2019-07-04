from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from django.views.generic import View
from .utils import *
from .forms import *


def tracks_list(request):
    tracks = Tracks.objects.all().order_by('-data_pub')
    genres = Genre.objects.all()[:10]
    return render(request, 'tracks/index.html',
                  context={'tracks': tracks,
                           'genres': genres,
                           'manage_panel': True,
                           'manage_panel_UD': False})


def top_list(request):
    tracks = Tracks.objects.all().order_by('-data_pub')[:2]
    return render(request, 'tracks/home_page.html',
                  context={'tracks': tracks,
                           'manage_panel': True,
                           'manage_panel_UD': False})


class TrackDetail(DetailMixin, View):
    model = Tracks
    template = 'tracks/track_detail.html'


class TrackCreate(ObjectCreateMixin, View):
    model = TrackForm
    template = 'tracks/track_create.html'


class TrackUpdate(ObjectUpdateMixin, View):
    model = Tracks
    template = 'tracks/track_update.html'
    model_form = TrackForm


class TrackDelete(ObjectDeleteMixin, View):
    model = Tracks
    template = 'tracks/track_delete.html'
    redirect_url = 'tracks_list_url'


def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'tracks/genres_list.html',
                  context={'genres': genres,
                           'manage_panel': True,
                           'manage_panel_UD': False})


class GenreDetail(DetailMixin, View):
    model = Genre
    template = 'tracks/genre_detail.html'


class GenreCreate(ObjectCreateMixin, View):
    model = GenreForm
    template = 'tracks/genre_create.html'


class GenreUpdate(ObjectUpdateMixin, View):
    model = Genre
    template = 'tracks/genre_update.html'
    model_form = GenreForm


class GenreDelete(ObjectDeleteMixin, View):
    model = Genre
    template = 'tracks/genre_delete.html'
    redirect_url = 'tracks_list_url'
