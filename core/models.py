from django.db import models

# Create your models here.
class MVV(models.Model):
    missao_texto = models.TextField('Texto para descrever a missão da empresa', max_length=200, null=False,);
    visao_texto = models.TextField('Texto para descrever a visão da empresa', max_length=200, null=False);
    valor_texto = models.TextField('Texto para descrever os valores da empresa', max_length=200, null=False);

    class Meta:
        verbose_name = 'MVV'   
        verbose_name_plural = 'MVV'   

    def __str__(self):
        return "Sobre a Biotech"

class Banner(models.Model):
    banner_image = models.ImageField("Imagem", upload_to = 'banner/', null=False)
    banner_titulo = models.CharField('Título', max_length=20, null=False,);
    banner_descricao = models.TextField('Descrição', max_length=200, null=False,);

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.banner_titulo