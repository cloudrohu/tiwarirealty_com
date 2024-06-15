# Generated by Django 5.0.1 on 2024-01-27 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('featured_builder', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.city')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.locality')),
            ],
            options={
                'verbose_name_plural': '4. Agency',
            },
        ),
        migrations.CreateModel(
            name='Agency_Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.agency')),
            ],
            options={
                'verbose_name_plural': '6. Agency Error',
            },
        ),
        migrations.CreateModel(
            name='Agency_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.agency')),
                ('social_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.social_site')),
            ],
            options={
                'verbose_name_plural': '5. Agency Link',
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('featured_builder', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.city')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.locality')),
            ],
            options={
                'verbose_name_plural': '1. Developer',
            },
        ),
        migrations.CreateModel(
            name='Developer_Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.developer')),
            ],
            options={
                'verbose_name_plural': '3. Developer Error',
            },
        ),
        migrations.CreateModel(
            name='Developer_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('Developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.developer')),
                ('social_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.social_site')),
            ],
            options={
                'verbose_name_plural': '2. Developer Link',
            },
        ),
    ]