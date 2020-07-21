from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView

from .forms import *
from .models import News, Musician, MusicalInstrument, Song, Band
from .utils import AdvancedListView, AdvancedDetailView, AdvancedTemplateView


class AboutPage(AdvancedTemplateView):
    template_name = 'music_portal/about_page'


class BandCreate(CreateView):
    template_name = "music_portal/content_create/band_create.html"
    form_class = BandCreateForm


class BandDetail(AdvancedDetailView):
    model = Band
    template_name = 'music_portal/content_detail/band_detail.html'


class BandList(AdvancedListView):
    template_name = 'music_portal/content_list/bands.html'
    paginate_by = 12
    model = Band


class ContactPage(AdvancedTemplateView):
    template_name = 'music_portal/contacts.html'   


class MainPage(AdvancedTemplateView):
    template_name = 'music_portal/index.html'
    

class MusicalInstrumentCreate(CreateView):
    template_name = "music_portal/content_create/musical_instrument_create.html"
    form_class = MusicalInstrumentCreateForm


class MusicalInstrumentDetail(AdvancedDetailView):
    model = MusicalInstrument
    template_name = 'music_portal/content_detail/musical_instrument_detail.html'
    context_object_name = 'musical_instrument'


class MusicalInstrumentDelete(DeleteView):
    template_name = "music_portal/content_delete/musical_instrument_delete.html"
    model = MusicalInstrument
    success_url = '/'


class MusicalInstrumentList(AdvancedListView):
    template_name = 'music_portal/content_list/musical_instruments.html'
    paginate_by = 12
    model = MusicalInstrument


class MusicalInstrumentUpdate(UpdateView):
    template_name = "music_portal/content_update/musical_instrument_update.html"
    form_class = MusicalInstrumentCreateForm
    model = MusicalInstrument


class MusicianCreate(CreateView):
    template_name = "music_portal/content_create/musician_create.html"
    form_class = MusicianCreateForm


class MusicianDetail(AdvancedDetailView):
    model = Musician
    template_name = "music_portal/content_detail/musician_detail.html"


class MusicianList(AdvancedListView):
    template_name = 'music_portal/content_list/musicians.html'
    paginate_by = 12
    model = Musician


class NewsCreate(CreateView):
    template_name = "music_portal/content_create/news_create.html"
    form_class = NewsCreateForm


class NewsDetail(AdvancedDetailView):
    model = News
    template_name = 'music_portal/content_detail/news_detail.html'


class NewsList(AdvancedListView):
    template_name = 'music_portal/content_list/news.html'
    paginate_by = 2
    model = News


class PrivacyPage(AdvancedTemplateView):
    template_name = 'music_portal/privacy.html'


class SongPage(AdvancedListView):
    template_name = 'music_portal/content_list/songs.html'
    paginate_by = 10
    model = Song


class SongCreate(CreateView):
    template_name = "music_portal/content_create/song_create.html"
    form_class = SongCreateForm


class UserTermsPage(AdvancedTemplateView):
    template_name = 'music_portal/user_terms.html'
