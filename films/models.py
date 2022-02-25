from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=200, null = True)
    category = models.CharField(max_length=200, null = True)
    description = models.CharField(max_length=9000000, null = True, blank=True)
    year = models.IntegerField(null=True)
    piattaforma = models.CharField(max_length=2000, null=True)
    date_added = models.DateTimeField(auto_now_add = True, null=True)
    objects = models.Manager()
    liked = models.ManyToManyField(User, default=None, blank =True, related_name='liked')
    watch = models.ManyToManyField(User, default=None, blank =True, related_name='watch')
    film_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    value = models.BooleanField(default=True)
    objects = models.Manager()


class Seen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    value = models.BooleanField(default=True)
    objects = models.Manager()


class Tip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    comment = models.CharField(max_length=20000000, null=True)
    stars = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    objects = models.Manager()