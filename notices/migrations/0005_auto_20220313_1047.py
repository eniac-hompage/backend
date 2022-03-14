# Generated by Django 3.2.7 on 2022-03-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0004_alter_notice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='desc',
            field=models.TextField(max_length=300, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='thumnail_img',
            field=models.ImageField(upload_to='', verbose_name='썸네일'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
    ]
