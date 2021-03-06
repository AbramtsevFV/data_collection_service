# Generated by Django 3.2 on 2021-09-02 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Имя пользователя',
                'verbose_name_plural': 'Имена пользоватедей',
            },
        ),
        migrations.CreateModel(
            name='RepoModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.CharField(max_length=256, verbose_name='Репозиторий')),
                ('read_me', models.TextField(verbose_name='read me')),
                ('created', models.CharField(max_length=20, verbose_name='Дата создания')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_user', to='service.usermodels')),
            ],
            options={
                'verbose_name': 'Репозиторий',
                'verbose_name_plural': 'Репозитории',
            },
        ),
    ]
