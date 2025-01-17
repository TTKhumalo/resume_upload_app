# Generated by Django 5.0.7 on 2024-07-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='summary',
            field=models.TextField(default=None),
        ),
    ]
