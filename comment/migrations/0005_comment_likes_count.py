# Generated by Django 3.2 on 2023-06-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_like_likecompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]