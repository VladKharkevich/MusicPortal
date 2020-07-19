from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import NewsCreateForm
from .models import News, Musician, MusicalInstrument, Song, Band
from .utils import AdvancedListView, AdvancedDetailView, AdvancedTemplateView


class AboutPage(AdvancedTemplateView):
    template_name = 'music_portal/about_page'


class BandList(AdvancedListView):
    template_name = 'music_portal/bands.html'
    paginate_by = 12
    model = Band


class BandDetail(AdvancedDetailView):
    model = Band


class ContactPage(AdvancedTemplateView):
    template_name = 'music_portal/contacts.html'   


class MainPage(AdvancedTemplateView):
    template_name = 'music_portal/index.html'
    

class MusicalInstrumentDetail(AdvancedDetailView):
    model = MusicalInstrument
    template_name = 'music_portal/musical_instrument_detail.html'
    context_object_name = 'musical_instrument'


class MusicalInstrumentList(AdvancedListView):
    template_name = 'music_portal/musical_instruments.html'
    paginate_by = 12
    model = MusicalInstrument


class MusicianList(AdvancedListView):
    template_name = 'music_portal/musicians.html'
    paginate_by = 12
    model = Musician


class MusicianDetail(AdvancedDetailView):
    model = Musician


class NewsCreate(View):
    def get(self, request):
        form = NewsCreateForm()
        return render(request, 'music_portal/news_create.html', context={'form': form})

    def post(self, request):
        bound_form = NewsCreateForm(request.POST)
        if bound_form.is_valid():
            new_news = bound_form.save()
            return redirect(new_news)
        return render(request, 'music_portal/news_create.html', context={'form': bound_form})


class NewsDetail(AdvancedDetailView):
    model = News

class NewsList(AdvancedListView):
    template_name = 'music_portal/news.html'
    paginate_by = 2
    model = News


class PrivacyPage(AdvancedTemplateView):
    template_name = 'music_portal/privacy.html'


class SongPage(AdvancedListView):
    template_name = 'music_portal/songs.html'
    paginate_by = 10
    model = Song


class UserTermsPage(AdvancedTemplateView):
    template_name = 'music_portal/user_terms.html'
