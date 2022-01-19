from email.headerregistry import Group
from django.contrib import admin

from .models import Encadreur, Promoteur, Groupe, Stagier, Organisme, Stage, typeStage


admin.site.register(Organisme)
admin.site.register(Encadreur)
admin.site.register(Promoteur)
admin.site.register(Groupe)
admin.site.register(Stagier)
admin.site.register(typeStage)
admin.site.register(Stage)


