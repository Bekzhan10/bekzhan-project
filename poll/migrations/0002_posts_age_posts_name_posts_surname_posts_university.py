# Generated by Django 4.0.2 on 2022-04-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.CharField(default='Beka', max_length=255),
        ),
        migrations.AddField(
            model_name='posts',
            name='surname',
            field=models.CharField(default='Turar', max_length=255),
        ),
        migrations.AddField(
            model_name='posts',
            name='university',
            field=models.CharField(default='SDU', max_length=255),
        ),
    ]
