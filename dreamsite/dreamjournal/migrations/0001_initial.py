# Generated by Django 3.2.3 on 2021-06-30 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, choices=[('Dream', 'Dream'), ('Nightmare', 'Nightmare')], max_length=10)),
                ('category', models.CharField(blank=True, choices=[('Reality', 'Reality'), ('Fantasy/Unreal', 'Fantasy/Unreal')], max_length=15)),
                ('colors_seen', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Orange', 'Orange'), ('Violet', 'Violet'), ('Brown', 'Brown'), ('Black', 'Black'), ('White', 'White')], max_length=53)),
                ('privacy', models.IntegerField(choices=[(0, 'Public'), (1, 'Private')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dreamjournal.journalpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]