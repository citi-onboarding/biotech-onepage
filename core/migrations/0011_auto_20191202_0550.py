# Generated by Django 2.2.7 on 2019-12-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191202_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(upload_to='banner/', verbose_name='Imagem'),
        ),
    ]
