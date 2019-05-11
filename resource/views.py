from django.views.generic.base import TemplateView

from resource.models import KeyManager


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tfidf'] = KeyManager.get_unused_key()

        return context
