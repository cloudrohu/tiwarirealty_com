# Generated by Django 5.0.1 on 2024-01-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fine_From',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': '19. Fine_From',
            },
        ),
    ]
