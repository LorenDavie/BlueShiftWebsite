""" 
Admin for blueweb.
"""

from blueweb import models
from django.contrib import admin

admin.site.register(models.Release)
admin.site.register(models.Song)
admin.site.register(models.BlogPost)
admin.site.register(models.Venue)
admin.site.register(models.Show)