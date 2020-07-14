from django.shortcuts import render, get_object_or_404
from django.views.generic import View

import datetime

from .models import News, Musician, MusicalInstrument, Song, Band


class AboutPage(View):
    def get(self, request):
        return render(request, 'music_portal/about.html')


class BandList(View):
    def get(self, request):
        bands = Band.objects.all()
        today = datetime.datetime.now()
        return render(request, 'music_portal/bands.html', context={'bands': bands,
                                                                   'today': today})


class BandDetail(View):
    def get(self, request, slug):
        obj = get_object_or_404(Band, slug__iexact=slug)
        return render(request, 'music_portal/band_detail.html',
                      context={Band.__name__.lower(): obj})


class ContactPage(View):
    def get(self, request):
        return render(request, 'music_portal/contacts.html')


class MainPage(View):
    def get(self, request):
        return render(request, 'music_portal/index.html')


class MusicalInstrumentDetail(View):
    def get(self, request, slug):
        obj = get_object_or_404(MusicalInstrument, slug__iexact=slug)
        return render(request, 'music_portal/musical_instrument_detail.html',
                      context={MusicalInstrument.__name__: obj})


class MusicalInstrumentList(View):
    def get(self, request):
        musical_instruments = MusicalInstrument.objects.all()
        return render(request, 'music_portal/musical_instruments.html', context={'musical_instruments': musical_instruments})


class MusicianList(View):
    def get(self, request):
        musicians = Musician.objects.all()
        today = datetime.datetime.now()
        return render(request, 'music_portal/musicians.html', context={'musicians': musicians,
                                                                       'today': today})


class MusicianDetail(View):
    def get(self, request, slug):
        obj = get_object_or_404(Musician, slug__iexact=slug)
        return render(request, 'music_portal/musician_detail.html',
                      context={Musician.__name__.lower(): obj})


class NewsList(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, 'music_portal/news.html', context={'news': news})


class PrivacyPage(View):
    def get(self, request):
        return render(request, 'music_portal/privacy.html')


class SongPage(View):
    def get(self, request):
        songs = Song.objects.all()
        return render(request, 'music_portal/songs.html', context={'songs': songs})


class UserTermsPage(View):
    def get(self, request):
        return render(request, 'music_portal/user_terms.html')
