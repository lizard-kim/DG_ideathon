# Generated by Django 3.0.6 on 2020-05-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20200516_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='job',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]