# Generated by Django 3.0.6 on 2020-05-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_auto_20200525_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fin',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]