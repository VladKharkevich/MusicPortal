from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import *
from .models import News, Musician, MusicalInstrument, Song, Band
from .utils import AdvancedListView, AdvancedDetailView, AdvancedTemplateView


class AboutPage(AdvancedTemplateView):
    template_name = 'music_portal/about_page'


class BandCreate(View):
    def get(self, request):
        form = BandCreateForm()
        return render(request, 'music_portal/content_create/band_create.html', 
                      context={'form': form})

    def post(self, request):
        bound_form = BandCreateForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_band = bound_form.save()
            return redirect(new_band)
        return render(request, 'music_portal/content_create/band_create.html', 
                      context={'form': bound_form})


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
    

class MusicalInstrumentCreate(View):
    def get(self, request):
        form = MusicalInstrumentCreateForm()
        return render(request, 'music_portal/content_create/musical_instrument_create.html', 
                      context={'form': form})

    def post(self, request):
        bound_form = MusicalInstrumentCreateForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_musical_instrument = bound_form.save()
            return redirect(new_musical_instrument)
        return render(request, 'music_portal/content_create/musical_instrument_create.html', 
                      context={'form': bound_form})


class MusicalInstrumentDetail(AdvancedDetailView):
    model = MusicalInstrument
    template_name = 'music_portal/content_detail/musical_instrument_detail.html'
    context_object_name = 'musical_instrument'


class MusicalInstrumentList(AdvancedListView):
    template_name = 'music_portal/content_list/musical_instruments.html'
    paginate_by = 12
    model = MusicalInstrument


class MusicianCreate(View):
    def get(self, request):
        form = MusicianCreateForm()
        return render(request, 'music_portal/content_create/musician_create.html', 
                      context={'form': form})

    def post(self, request):
        bound_form = MusicianCreateForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_musician = bound_form.save()
            return redirect(new_musician)
        return render(request, 'music_portal/content_create/musician_create.html', 
                      context={'form': bound_form})


class MusicianDetail(AdvancedDetailView):
    model = Musician
    template_name = "music_portal/content_detail/musician_detail.html"


class MusicianList(AdvancedListView):
    template_name = 'music_portal/content_list/musicians.html'
    paginate_by = 12
    model = Musician


class NewsCreate(View):
    def get(self, request):
        form = NewsCreateForm()
        return render(request, 'music_portal/content_create/news_create.html', context={'form': form})

    def post(self, request):
        bound_form = NewsCreateForm(request.POST)
        if bound_form.is_valid():
            new_news = bound_form.save()
            return redirect(new_news)
        return render(request, 'music_portal/content_create/news_create.html', context={'form': bound_form})


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


class SongCreate(View):
    def get(self, request):
        form = SongCreateForm()
        return render(request, 'music_portal/content_create/song_create.html', 
                      context={'form': form})

    def post(self, request):
        bound_form = SongCreateForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_song = bound_form.save()
            return redirect(reverse('song_page_url'))
        return render(request, 'music_portal/content_create/song_create.html', 
                      context={'form': bound_form})


class UserTermsPage(AdvancedTemplateView):
    template_name = 'music_portal/user_terms.html'
