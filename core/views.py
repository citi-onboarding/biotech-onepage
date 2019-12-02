from django.shortcuts import render
from django.views.generic import TemplateView
from templated_email import send_templated_mail
from django.http import HttpResponseRedirect

from core.models import *

import os
import environ
env = environ.Env()

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["mvv"] = MVV.objects.get()
        context["banner"] = Banner.objects.all()

        return context

def send_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        empresa = request.POST.get('empresa')
        area_atuacao = request.POST.get('area-atuacao')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        send_templated_mail(
            template_name='contact',
            from_email=email,
            recipient_list=[env('EMAIL_RECIPIENT_ACCOUNT'),env('EMAIL_RECIPIENT_ACCOUNT')],
            context={
                'nome':nome,
                'telefone':telefone,
                'email':email,
                'empresa':empresa,
                'area_atuacao':area_atuacao,
                'assunto': assunto,
                'mensagem': mensagem,
            }
        )

        return HttpResponseRedirect('/')

    return render(request,'core/index.html',{})