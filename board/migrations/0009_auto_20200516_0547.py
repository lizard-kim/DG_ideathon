# Generated by Django 3.0.6 on 2020-05-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20200516_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='board.Comment'),
        ),
    ]
