# Generated by Django 5.0 on 2023-12-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='time_duration',
            field=models.IntegerField(null=True),
        ),
    ]