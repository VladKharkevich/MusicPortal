from typing import Dict

from django.views.generic import ListView, DetailView, TemplateView

from .models import News


def base_page_context() -> Dict:
    """
    Function returns context that is used in base.html template:
    1. Returns 3 news in aside tag.
    """
    news = News.objects.all()[:3]
    context = {
        'aside_news': news
    }
    return context


class AdvancedListView(ListView):
    """
    This class overrides ListView method get_context_data. 
    To dict 'context' added keys about content that contains in every page.  
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **base_page_context()}


class AdvancedDetailView(DetailView):
    """
    This class overrides DetailView method get_context_data. 
    To dict 'context' added keys about content that contains in every page.  
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **base_page_context()}


class AdvancedTemplateView(TemplateView):
    """
    This class overrides TemplateView method get_context_data. 
    To dict 'context' added keys about content that contains in every page.  
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {**context, **base_page_context()}

