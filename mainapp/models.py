from django.db import models
from user.models import User


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Game(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128, unique=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='gamePhoto')
    genre = models.ForeignKey(Genre, to_field='name', verbose_name='Жанр', on_delete=models.CASCADE)
    video = models.ImageField(verbose_name='Видео', upload_to='gameVideo', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=2048)
    android = models.BooleanField(verbose_name='Android', default=False)
    ios = models.BooleanField(verbose_name='IOS', default=False)
    windows = models.BooleanField(verbose_name='Windows', default=False)
    psp = models.BooleanField(verbose_name='PSP', default=False)
    xbox = models.BooleanField(verbose_name='X-Box', default=False)
    rating = models.SmallIntegerField(verbose_name='Рейтинг', default=0)
    added = models.DateTimeField(verbose_name='Добавлена', auto_now_add=True)
    language = models.BooleanField(verbose_name='Русский язык', default=False)
    paidContent = models.BooleanField(verbose_name='Платный контент', default=False)

    advertising = models.BooleanField(verbose_name='Реклама', default=False)
    active = models.BooleanField(verbose_name='active', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['added', 'name']
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'


class Requirement(models.Model):
    game = models.ForeignKey(Game, to_field='name', verbose_name='Название', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game}'

    class Meta:
        ordering = ['game']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GamePhoto(models.Model):
    game = models.ForeignKey(Game, to_field='name', verbose_name='Название', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото', upload_to='gamePhoto')


class GameComment(models.Model):
    game = models.ForeignKey(Game, to_field='name', verbose_name='Название', on_delete=models.CASCADE)
    author = models.ForeignKey(User, to_field='email', verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Коментарий', blank=True, max_length=548)
    date_added = models.DateTimeField(verbose_name='Добавлен комментария', auto_now_add=True)
    photo = models.ImageField(verbose_name='Фото комментария', blank=True, upload_to='gameCommentPhoto')

    class Meta:
        ordering = ['game']
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class UserGame(models.Model):
    user = models.ForeignKey(User, to_field='id', verbose_name='Пользаватель', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, to_field='name', verbose_name='Название', on_delete=models.CASCADE)
