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


class Servicos(models.Model):
    servico_tipo = models.TextField('Texto para o nome do serviço', null=False);
    servico_descricao = models.TextField('Texto para descrever o serviço', null=False);
    servico_icone = models.ImageField('Ícone correspondente ao serviço', null=False);

    class Meta:
        verbose_name = 'Servicos'     

    def __str__(self):
        return "Nossos serviços"

class Banner(models.Model):
    banner_image = models.ImageField("Imagem", upload_to = 'banner/', null=False)
    banner_titulo = models.CharField('Título', max_length=20, null=False,);
    banner_descricao = models.TextField('Descrição', max_length=200, null=False,);

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.banner_titulo
