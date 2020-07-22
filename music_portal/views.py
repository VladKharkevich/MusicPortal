from .forms import *
from .models import News, Musician, MusicalInstrument, Song, Band
from .utils import AdvancedListView, AdvancedDetailView, AdvancedTemplateView
from .utils import AdvancedCreateView, AdvancedUpdateView, AdvancedDeleteView


class AboutPage(AdvancedTemplateView):
    template_name = 'music_portal/about_page'


class BandCreate(AdvancedCreateView):
    template_name = "music_portal/content_create/band_create.html"
    form_class = BandForm


class BandDelete(AdvancedDeleteView):
    template_name = "music_portal/content_delete/band_delete.html"
    model = Band
    success_url = '/'


class BandDetail(AdvancedDetailView):
    model = Band
    template_name = 'music_portal/content_detail/band_detail.html'


class BandList(AdvancedListView):
    template_name = 'music_portal/content_list/bands.html'
    paginate_by = 12
    model = Band


class BandUpdate(AdvancedUpdateView):
    template_name = "music_portal/content_update/band_update.html"
    form_class = BandForm
    model = Band


class ContactPage(AdvancedTemplateView):
    template_name = 'music_portal/contacts.html'   


class MainPage(AdvancedTemplateView):
    template_name = 'music_portal/index.html'
    

class MusicalInstrumentCreate(AdvancedCreateView):
    template_name = "music_portal/content_create/musical_instrument_create.html"
    form_class = MusicalInstrumentForm


class MusicalInstrumentDelete(AdvancedDeleteView):
    template_name = "music_portal/content_delete/musical_instrument_delete.html"
    model = MusicalInstrument
    success_url = '/'


class MusicalInstrumentDetail(AdvancedDetailView):
    model = MusicalInstrument
    template_name = 'music_portal/content_detail/musical_instrument_detail.html'
    context_object_name = 'musical_instrument'


class MusicalInstrumentList(AdvancedListView):
    template_name = 'music_portal/content_list/musical_instruments.html'
    paginate_by = 12
    model = MusicalInstrument


class MusicalInstrumentUpdate(AdvancedUpdateView):
    template_name = "music_portal/content_update/musical_instrument_update.html"
    form_class = MusicalInstrumentForm
    model = MusicalInstrument


class MusicianCreate(AdvancedCreateView):
    template_name = "music_portal/content_create/musician_create.html"
    form_class = MusicianForm


class MusicianDelete(AdvancedDeleteView):
    template_name = "music_portal/content_delete/musician_delete.html"
    model = Musician
    success_url = '/'


class MusicianDetail(AdvancedDetailView):
    model = Musician
    template_name = "music_portal/content_detail/musician_detail.html"


class MusicianList(AdvancedListView):
    template_name = 'music_portal/content_list/musicians.html'
    paginate_by = 12
    model = Musician


class MusicianUpdate(AdvancedUpdateView):
    template_name = "music_portal/content_update/musician_update.html"
    form_class = MusicianForm
    model = Musician


class NewsCreate(AdvancedCreateView):
    template_name = "music_portal/content_create/news_create.html"
    form_class = NewsForm


class NewsDelete(AdvancedDeleteView):
    model = News
    template_name = 'music_portal/content_delete/news_delete.html'
    success_url = '/'


class NewsDetail(AdvancedDetailView):
    model = News
    template_name = 'music_portal/content_detail/news_detail.html'


class NewsList(AdvancedListView):
    template_name = 'music_portal/content_list/news.html'
    paginate_by = 2
    model = News


class NewsUpdate(AdvancedUpdateView):
    model = News
    form_class = NewsForm
    template_name = 'music_portal/content_update/news_update.html'


class PrivacyPage(AdvancedTemplateView):
    template_name = 'music_portal/privacy.html'


class SongCreate(AdvancedCreateView):
    template_name = "music_portal/content_create/song_create.html"
    form_class = SongForm


class SongDelete(AdvancedDeleteView):
    model = Song
    template_name = "music_portal/content_delete/song_delete.html"
    success_url = '/'


class SongPage(AdvancedListView):
    template_name = 'music_portal/content_list/songs.html'
    paginate_by = 10
    model = Song


class SongUpdate(AdvancedUpdateView):
    template_name = "music_portal/content_update/song_update.html"
    form_class = SongForm
    model = Song


class UserTermsPage(AdvancedTemplateView):
    template_name = 'music_portal/user_terms.html'
