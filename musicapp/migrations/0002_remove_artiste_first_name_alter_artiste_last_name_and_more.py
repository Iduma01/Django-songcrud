# Generated by Django 4.1.2 on 2022-10-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artiste',
            name='First_name',
        ),
        migrations.AlterField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=225),
        ),
        migrations.AddField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
