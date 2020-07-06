from django.urls import path

from .views import index, news_view, musicians_view


urlpatterns = [
    path('', index),
    path('news/', news_view),
    path('musicians/', musicians_view)
]
