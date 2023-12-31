# Generated by Django 3.2 on 2023-06-21 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0018_auto_20230621_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likecompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='account.student')),
                ('likeuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='account.company')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislikecompany', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dislikes', to='account.student')),
                ('dislikeuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dislike', to='account.company')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.company', verbose_name='company')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='account.student')),
            ],
        ),
    ]
