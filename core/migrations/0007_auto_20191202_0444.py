# Generated by Django 2.2.7 on 2019-12-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191202_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(default='banner/default.jpg', upload_to='banner/'),
        ),
    ]
