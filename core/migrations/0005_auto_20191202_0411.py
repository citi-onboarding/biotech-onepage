# Generated by Django 2.2.7 on 2019-12-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191202_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_descricao',
            field=models.TextField(max_length=100, verbose_name='Descrição'),
        ),
    ]