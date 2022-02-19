# Generated by Django 3.2.7 on 2022-02-09 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0011_auto_20220207_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(max_length=300)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Challenge_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(max_length=300)),
                ('challenge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_comments', to='activities.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='challenge_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'challenge_comments',
            },
        ),
    ]
