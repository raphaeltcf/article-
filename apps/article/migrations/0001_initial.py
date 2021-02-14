# Generated by Django 3.1.6 on 2021-02-14 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Autor')),
                ('email', models.EmailField(max_length=254, verbose_name='Email do Autor')),
            ],
            options={
                'verbose_name_plural': 'Autor',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=120, verbose_name='Titulo do artigo')),
                ('descripition', models.TextField(verbose_name='Descrição')),
                ('body', models.TextField(verbose_name='Texto')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.author', verbose_name='Autor do texto')),
            ],
            options={
                'verbose_name_plural': 'Artigo',
            },
        ),
    ]
