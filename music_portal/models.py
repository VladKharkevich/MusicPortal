from django.db import models
from django.shortcuts import reverse
from django.contrib.postgres.fields import JSONField


class News(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-published"]


"""
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
"""


class MusicalInstrument(models.Model):
    TYPES_OF_INSTRUMENT = (
        ('s', 'stringed'),
        ('w', 'wind'),
        ('e', 'electronic'),
        ('p', 'percussion'),
        ('o', 'other')
    )
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='musical_instrument_photos')
    type_of_instrument = models.CharField(max_length=1, choices=TYPES_OF_INSTRUMENT, db_index=True)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('musical_instrument_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True)
    songfile = models.FileField(upload_to='song_audio')
    year_of_creation = models.PositiveSmallIntegerField(default=2020)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Musician(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    biography = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='musician_photos', blank=True)
    songs = models.ManyToManyField(Song, related_name='musicians')

    def get_absolute_url(self):
        return reverse('musician_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Band(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    biography = models.TextField(null=True, blank=True)
    date_of_creation = models.PositiveSmallIntegerField(default=2020)
    date_of_breakup = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='band_photos', blank=True)
    members = models.ManyToManyField(Musician, related_name='bands')
    songs = models.ManyToManyField(Song, related_name='bands', blank=True)

    def get_absolute_url(self):
        return reverse('band_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class VotingBallot(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    votes = JSONField()

    def __str__(self):
        return self.title
