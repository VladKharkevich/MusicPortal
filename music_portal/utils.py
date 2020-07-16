from typing import Dict

from django.core.paginator import Paginator

from .models import News


def base_page_context() -> Dict:
    """Function returns context that is used in base.html template:
        1. Returns 3 news in aside tag"""
    news = News.objects.all()[:3]
    context = {
        'aside_news': news
    }
    return context


def connecting_paginator(request, query_set, number_of_records: int) -> Dict:
    """ Function connects paginator and return a dictionary, 
        important for paginator.html
        query_set is a data, received from database"""
    paginator = Paginator(query_set, number_of_records)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = f"?page={page.previous_page_number()}"
    else:
        prev_url = ""

    if page.has_next():
        next_url = f"?page={page.next_page_number()}"
    else:
        next_url = ""

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return context