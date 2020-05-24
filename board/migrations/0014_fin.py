# Generated by Django 3.0.6 on 2020-05-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20200519_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('team', models.CharField(max_length=50)),
                ('leader', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
                ('writer', models.CharField(max_length=50)),
                ('motivation', models.TextField(blank=True, max_length=500)),
                ('process', models.TextField(blank=True, max_length=500)),
                ('expectation', models.TextField(blank=True, max_length=500)),
                ('file', models.TextField(max_length=500)),
                ('video', models.TextField(max_length=500)),
            ],
        ),
    ]