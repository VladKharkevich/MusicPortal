from django.shortcuts import render
from django.views.generic import View


class MainPage(View):
    def get(self, request):
        return render(request, 'music_portal/index.html')


class NewsList(View):
    def get(self, request):
        return render(request, 'music_portal/news.html')


class MusicianList(View):
    def get(self, request):
        return render(request, 'music_portal/musicians.html')


class MusicalInstrumentList(View):
    def get(self, request):
        return render(request, 'music_portal/musical_instruments.html')


class ContactPage(View):
    def get(self, request):
        return render(request, 'music_portal/contacts.html')
