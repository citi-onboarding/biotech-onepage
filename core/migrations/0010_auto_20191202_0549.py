# Generated by Django 2.2.7 on 2019-12-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191202_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(upload_to='', verbose_name='Imagem'),
        ),
    ]