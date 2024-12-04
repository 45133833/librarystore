# Generated by Django 5.1.2 on 2024-10-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('auther', models.CharField(default='guest', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('description', models.TextField(default='available', max_length=500)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]