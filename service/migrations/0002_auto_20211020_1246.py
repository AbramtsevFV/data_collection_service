# Generated by Django 3.2 on 2021-10-20 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repomodels',
            name='created',
            field=models.CharField(max_length=30, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='repomodels',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository', to='service.usermodels'),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Имя пользователя'),
        ),
    ]