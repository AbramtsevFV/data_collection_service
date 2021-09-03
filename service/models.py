from django.db import models

class UserModels(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя пользователя'
        verbose_name_plural = 'Имена пользоватедей'

class RepoModels(models.Model):
    name = models.ForeignKey(UserModels, related_name='repository', on_delete=models.CASCADE)
    repo = models.CharField(verbose_name='Репозиторий', max_length=256)
    read_me =  models.TextField(verbose_name='read me')
    created = models.CharField(verbose_name='Дата создания', max_length=30)

    def __str__(self):
        return self.repo

    class Meta:
            verbose_name = "Репозиторий"
            verbose_name_plural = "Репозитории"