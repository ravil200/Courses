from django.contrib.auth.models import User as Clients
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Language(models.Model):
    language = models.CharField(max_length=100)
    teach = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teach')
    price = models.FloatField()

    def __str__(self):
        return self.language



class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()
    adress = models.TextField()
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Comment(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='grades', verbose_name='Клиент')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='grade_teacher')
    comment = models.TextField(help_text=f'Оставьте отзыв о преподавателе', max_length=500)

    def __str__(self):
        return self.clients.username

    class Meta:
        verbose_name_plural = 'Отзыв'

class Lesson(models.Model):
    class_room_number = models.IntegerField()
    teach = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)