from django.urls import path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page_url'),
    path('about/', AboutPage.as_view(), name='about_page_url'),

    path('bands/', BandList.as_view(), name='bands_url'),
    path('bands/create/', BandCreate.as_view(), name='band_create_url'),
    path('bands/<str:slug>/', BandDetail.as_view(), name='band_detail_url'),
    path('bands/<str:slug>/update/', BandUpdate.as_view(), name='band_update_url'),
    path('bands/<str:slug>/delete/', BandDelete.as_view(), name='band_delete_url'),

    path('contacts/', ContactPage.as_view(), name='contacts_url'),

    path('musical-instruments/', MusicalInstrumentList.as_view(),
         name='musical_instruments_page_url'),
    path('musical-instruments/create/', MusicalInstrumentCreate.as_view(), 
         name='musical_instrument_create_url'),
    path('musical-instruments/<str:slug>/', MusicalInstrumentDetail.as_view(),
         name='musical_instrument_detail_url'),
    path('musical-instruments/<str:slug>/update/', MusicalInstrumentUpdate.as_view(),
         name='musical_instrument_update_url'),
    path('musical-instruments/<str:slug>/delete/', MusicalInstrumentDelete.as_view(),
         name='musical_instrument_delete_url'),

    path('musicians/', MusicianList.as_view(), name='musicians_page_url'),
    path('musicians/create/', MusicianCreate.as_view(), name='musician_create_url'),
    path('musicians/<str:slug>/', MusicianDetail.as_view(), name='musician_detail_url'),
    path('musicians/<str:slug>/update/', MusicianUpdate.as_view(),
         name='musician_update_url'),
    path('musicians/<str:slug>/delete/', MusicianDelete.as_view(),
         name='musician_delete_url'),

    path('news/', NewsList.as_view(), name='news_page_url'),
    path('news/create/', NewsCreate.as_view(), name='news_create_url'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news_detail_url'),
    path('news/<str:slug>/update/', NewsUpdate.as_view(), name='news_update_url'),
    path('news/<str:slug>/delete/', NewsDelete.as_view(), name='news_delete_url'),
    
    path('privacy/', PrivacyPage.as_view(), name='privacy_page_url'),
    
    path('songs/', SongPage.as_view(), name='songs_page_url'),
    path('songs/create/', SongCreate.as_view(), name='song_create_url'),
    path('songs/<str:slug>/update/', SongUpdate.as_view(), name='song_update_url'),
    path('songs/<str:slug>/delete/', SongDelete.as_view(), name='song_delete_url'),
    
    path('user-terms/', UserTermsPage.as_view(), name='user_terms_page_url'),
]
