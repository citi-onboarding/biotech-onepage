from django.db import models
from solo.models import SingletonModel

# Create your models here.
class MVV(SingletonModel):
    missao_texto = models.TextField('Texto para descrever a missão da empresa', max_length=200, null=False,);
    visao_texto = models.TextField('Texto para descrever a visão da empresa', max_length=200, null=False);
    valor_texto = models.TextField('Texto para descrever os valores da empresa', max_length=200, null=False);

    class Meta:
        verbose_name = 'MVV'     

    def __str__(self):
        return "Sobre a Biotech"