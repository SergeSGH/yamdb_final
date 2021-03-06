# Generated by Django 3.0 on 2021-11-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Категория произведения', max_length=200, verbose_name='Категория произведения')),
                ('slug', models.SlugField(help_text='Слаг категории', unique=True, verbose_name='Слаг категории')),
                ('description', models.TextField(blank=True, help_text='Описание', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название жанра', max_length=200, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Слаг жанра', unique=True, verbose_name='Слаг жанра')),
                ('description', models.TextField(blank=True, help_text='Описание', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='yamdb.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название произведения', max_length=200, verbose_name='Название произведения')),
                ('year', models.IntegerField(help_text='Год выпуска произведения', verbose_name='Год выпуска произведения')),
                ('description', models.TextField(blank=True, help_text='Описание', null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(help_text='Категория произведения', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='yamdb.Category', verbose_name='Категория произведения')),
                ('genre', models.ManyToManyField(help_text='Жанр произведения', through='yamdb.GenreTitle', to='yamdb.Genre', verbose_name='Жанр произведения')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведение',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='yamdb.Title'),
        ),
        migrations.AddConstraint(
            model_name='genretitle',
            constraint=models.UniqueConstraint(fields=('genre', 'title'), name='unique_genretitle'),
        ),
    ]
