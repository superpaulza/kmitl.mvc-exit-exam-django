# Generated by Django 4.0.3 on 2022-03-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meme',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meme',
            name='reach',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meme',
            name='share',
            field=models.IntegerField(default=0),
        ),
    ]