# Generated by Django 3.1.5 on 2021-04-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210325_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(help_text='The the reviewer has given.'),
        ),
    ]
