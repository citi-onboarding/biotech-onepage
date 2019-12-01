from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import *

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["mvv"] = MVV.objects.get()

        return context