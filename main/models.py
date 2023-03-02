from django.db import models


# Create your models here.
class Student(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия', null=True)
    name = models.CharField(max_length=50, verbose_name='Имя', null=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    group = models.ForeignKey('Group', related_name='student', on_delete=models.CASCADE, verbose_name='Группа',
                              null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    direction = models.CharField(max_length=50, verbose_name='Направление')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
