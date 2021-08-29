# Generated by Django 3.2.6 on 2021-08-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='nutritionGuides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nutrition Guides',
            },
        ),
    ]