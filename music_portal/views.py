from django.shortcuts import render
from django.views.generic import View


class AboutPage(View):
    def get(self, request):
        return render(request, 'music_portal/about.html')


class ContactPage(View):
    def get(self, request):
        return render(request, 'music_portal/contacts.html')


class MainPage(View):
    def get(self, request):
        return render(request, 'music_portal/index.html')


class MusicalInstrumentList(View):
    def get(self, request):
        return render(request, 'music_portal/musical_instruments.html')


class MusicianList(View):
    def get(self, request):
        return render(request, 'music_portal/musicians.html')


class NewsList(View):
    def get(self, request):
        return render(request, 'music_portal/news.html')


class PrivacyPage(View):
    def get(self, request):
        return render(request, 'music_portal/privacy.html')


class SongPage(View):
    def get(self, request):
        return render(request, 'music_portal/songs.html')


class UserTermsPage(View):
    def get(self, request):
        return render(request, 'music_portal/user_terms.html')
