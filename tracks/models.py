from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s)
    return new_slug + '-' + str(int(time()))


class Tracks(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField()
    performer = models.CharField(max_length=150, db_index=True)
    genres = models.ManyToManyField('Genre', blank=True, related_name='tracks')
    data_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('track_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('track_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('track_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)

        super(Tracks, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tracks"


class Genre(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('genre_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('genre_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('genre_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = "Genres"
