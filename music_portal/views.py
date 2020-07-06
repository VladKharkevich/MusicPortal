from django.shortcuts import render


def index(request):
    return render(request, 'music_portal/index.html')


def news_view(request):
    return render(request, 'music_portal/news.html')


def musicians_view(request):
    return render(request, 'music_portal/musicians.html')
