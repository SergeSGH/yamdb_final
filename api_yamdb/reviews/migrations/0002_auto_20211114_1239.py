# Generated by Django 3.0 on 2021-11-14 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
        ('yamdb', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(help_text='Автор ревью', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор ревью'),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.ForeignKey(help_text='Произведение', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='yamdb.Title', verbose_name='Произведение'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='Автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(help_text='отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='отзыв'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_review'),
        ),
    ]
