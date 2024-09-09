from django.contrib import admin

from .models import Grzyby, Rodzina, Potrawy

admin.site.register(Grzyby)
admin.site.register(Rodzina)
admin.site.register(Potrawy)