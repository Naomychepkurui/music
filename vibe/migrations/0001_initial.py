# Generated by Django 3.1 on 2021-02-28 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=500)),
                ('album_title', models.CharField(max_length=500)),
                ('album_log', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=500)),
                ('audio_file', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vibe.album')),
            ],
        ),
    ]