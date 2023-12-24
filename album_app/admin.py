from django.contrib import admin
from .models import Album_Model, StarRatingModel, Instrument_Model

# Register your models here.
admin.site.register(StarRatingModel)
admin.site.register(Instrument_Model)
admin.site.register(Album_Model)
