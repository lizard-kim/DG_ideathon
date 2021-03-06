# Generated by Django 3.0.6 on 2020-05-12 22:30

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
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('contents', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('contents', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonymous', max_length=20)),
                ('birthday', models.DateField()),
                ('phonenumber', models.CharField(default='no number', max_length=20)),
                ('school', models.CharField(default='no school', max_length=20)),
                ('email', models.CharField(default='test@gmail.com', max_length=50)),
                ('address', models.CharField(default='address', max_length=60)),
                ('team', models.CharField(default='team', max_length=50)),
                ('auth', models.CharField(default='user', max_length=10)),
                ('idea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Idea')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
