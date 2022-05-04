from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Sandardy engizuge bolmaidy')


class Films(models.Model):
    film_name = models.CharField(max_length=200)
    film_year = models.IntegerField(default=0)


class Users(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)


class Genres(models.Model):
    genre_name = models.CharField(max_length=200)
    genre_id = models.IntegerField(default=0)

class Cartoons(models.Model):
    cartoon_id = models.IntegerField(default=0)
    cartoon_name = models.CharField(max_length = 200)

class Poll(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    producer = models.CharField(max_length=30, default= 'unknown')

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмдер"
        ordering = ['producer','title']

class Posts(models.Model):
    title = models.CharField( max_length=255, verbose_name="Тақырып")
    is_published = models.BooleanField(default=True, verbose_name="Шығарылым")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    university = models.CharField(max_length=255)

    def get_absolute_url(self):
            return reverse('post',kwargs={'post_slug':self.slug})

    def one_plus_two(self):
        return 3;