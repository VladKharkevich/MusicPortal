from django.db import models
from django.contrib.postgres.fields import JSONField


class News(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    content = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True, db_index=True)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class MusicalInstrument(models.Model):
    TYPES_OF_INSTRUMENT = (
        ('s', 'stringed'),
        ('w', 'wind'),
        ('e', 'electronic'),
        ('p', 'percussion'),
        ('o', 'other')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    photo = models.ImageField()
    type_of_instrument = models.CharField(max_length=1, choices=TYPES_OF_INSTRUMENT)
    description = models.TextField(max_length=100, blank=True, unique=True)


class Album(models.Model):
    name = models.CharField(max_length=100)


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL)


class Mucisian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    biography = models.TextField()
    songs = models.ManyToManyField(Song)


class Band(models.Model):
    name = models.CharField(max_length=100)
    date_of_creation = models.DateField()
    date_of_breakup = models.DateField()
    members = models.ManyToManyField(Mucisian)
    biography = models.TextField()
    songs = models.ManyToManyField(Song)


class VotingBallot(models.Model):
    title = models.CharField(max_length=100)
    votes = JSONField()
