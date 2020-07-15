from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import News, Musician, MusicalInstrument, Song, Band
from .utils import base_page_context


class AboutPage(View):
    def get(self, request):
        context = base_page_context()
        return render(request, 'music_portal/about.html', context=context)


class BandList(View):
    def get(self, request):
        context = base_page_context()
        bands = Band.objects.all()
        context['bands'] = bands
        return render(request, 'music_portal/bands.html', context=context)


class BandDetail(View):
    def get(self, request, slug):
        context = base_page_context()
        obj = get_object_or_404(Band, slug__iexact=slug)
        context[Band.__name__.lower()] = obj
        return render(request, 'music_portal/band_detail.html', context=context)


class ContactPage(View):
    def get(self, request):
        context = base_page_context()
        return render(request, 'music_portal/contacts.html', context=context)


class MainPage(View):
    def get(self, request):
        context = base_page_context()
        return render(request, 'music_portal/index.html', context=context)


class MusicalInstrumentDetail(View):
    def get(self, request, slug):
        context = base_page_context()
        obj = get_object_or_404(MusicalInstrument, slug__iexact=slug)
        context[MusicalInstrument.__name__] = obj
        return render(request, 'music_portal/musical_instrument_detail.html', context=context)


class MusicalInstrumentList(View):
    def get(self, request):
        context = base_page_context()
        musical_instruments = MusicalInstrument.objects.all()
        context['musical_instruments'] = musical_instruments
        return render(request, 'music_portal/musical_instruments.html', context=context)


class MusicianList(View):
    def get(self, request):
        context = base_page_context()
        musicians = Musician.objects.all()
        context['musicians'] = musicians
        return render(request, 'music_portal/musicians.html', context=context)


class MusicianDetail(View):
    def get(self, request, slug):
        context = base_page_context()
        obj = get_object_or_404(Musician, slug__iexact=slug)
        context[Musician.__name__.lower()] = obj
        return render(request, 'music_portal/musician_detail.html', context=context)


class NewsList(View):
    def get(self, request):
        context = base_page_context()
        news = News.objects.all()
        context['news'] = news
        return render(request, 'music_portal/news.html', context=context)


class PrivacyPage(View):
    def get(self, request):
        context = base_page_context()
        return render(request, 'music_portal/privacy.html', context=context)


class SongPage(View):
    def get(self, request):
        context = base_page_context()
        songs = Song.objects.all()
        context['songs'] = songs
        return render(request, 'music_portal/songs.html', context=context)


class UserTermsPage(View):
    def get(self, request):
        context = base_page_context()
        return render(request, 'music_portal/user_terms.html', context=context)
