from typing import Dict

from .models import News


def base_page_context() -> Dict:
    """Function returns context that is used in base.html template:
        1. Returns 3 news in aside tag"""
    news = News.objects.all()[:3]
    context = {
        'aside_news': news
    }
    return context
