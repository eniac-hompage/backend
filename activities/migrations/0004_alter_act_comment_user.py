# Generated by Django 3.2.7 on 2022-03-19 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0003_auto_20220319_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act_comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
