# Generated by Django 3.0.6 on 2020-05-16 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20200516_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Comment'),
        ),
    ]
