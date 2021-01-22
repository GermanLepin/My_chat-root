from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import render
from django.views import View


class Chat(models.Model):
    """Модель комнаты чата"""
    creater = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="invited_user")
    date = models.DateTimeField("Дата создания", auto_now_add=True)


    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class Message(models.Model):
    """Модель чата"""
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


