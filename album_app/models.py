from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StarRatingModel(models.Model):
    rating = models.CharField(max_length=5)

    def __str__(self):
        return self.rating


class Instrument_Model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album_Model(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(User, on_delete=models.CASCADE)
    instruments = models.ManyToManyField(Instrument_Model)
    release_date = models.DateField()
    rating = models.ForeignKey(StarRatingModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    # python .\manage.py makemigrations
    # python .\manage.py migrate
    # python .\manage.py createsuperuser ★
