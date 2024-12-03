# Generated by Django 5.1.2 on 2024-11-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmCoP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='board/')),
                ('twitter_url', models.CharField(blank=True, max_length=60)),
                ('linkedin_url', models.CharField(blank=True, max_length=78)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='teams/')),
                ('twitter_url', models.CharField(blank=True, max_length=60)),
                ('instagram_url', models.CharField(blank=True, max_length=78)),
                ('facebook_url', models.CharField(blank=True, max_length=78)),
                ('linkedin_url', models.CharField(blank=True, max_length=78)),
            ],
        ),
    ]