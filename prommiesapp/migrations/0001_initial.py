# Generated by Django 4.0.5 on 2022-06-12 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prommies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('email', models.EmailField(max_length=254)),
                ('my_file', models.FileField(upload_to='doc')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='This is your bio')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')),
                ('mobile', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prommiesapp.prommies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
