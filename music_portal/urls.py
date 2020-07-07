from django.urls import path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page_url'),
    path('news/', NewsList.as_view(), name='news_page_url'),
    path('musicians/', MusicianList.as_view(), name='musicians_page_url'),
    path('musical-instruments/', MusicalInstrumentList.as_view(), name='musical_instruments_page_url'),
    path('contacts/', ContactPage.as_view(), name='contacts_url')
]
