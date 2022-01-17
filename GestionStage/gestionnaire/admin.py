from django.contrib import admin

from .models import Encadreur, Promoteur, Groupe, Stagier

admin.site.register(Encadreur)
admin.site.register(Promoteur)
admin.site.register(Groupe)
admin.site.register(Stagier)