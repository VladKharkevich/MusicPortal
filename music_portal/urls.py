from django.urls import path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page_url'),
    path('about/', AboutPage.as_view(), name='about_page_url'),
    path('contacts/', ContactPage.as_view(), name='contacts_url'),
    path('musical-instruments/', MusicalInstrumentList.as_view(),
         name='musical_instruments_page_url'),
    path('musical-instruments/<str:slug>/', MusicalInstrumentDetail.as_view(),
         name='musical_instrument_detail_url'),
    path('musicians/', MusicianList.as_view(), name='musicians_page_url'),
    path('musicians/<str:slug>/', MusicianDetail.as_view(), name='musician_detail_url'),
    path('news/', NewsList.as_view(), name='news_page_url'),
    # path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('privacy/', PrivacyPage.as_view(), name='privacy_page_url'),
    path('songs/', SongPage.as_view(), name='songs_page_url'),
    path('user-terms/', UserTermsPage.as_view(), name='user_terms_page_url'),
]
