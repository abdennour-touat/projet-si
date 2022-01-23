from django.contrib import admin

from .models import Encadreur, Promoteur, Groupe, Stagier, Organisme, Stage, TypeStage


admin.site.register(Organisme)
admin.site.register(Encadreur)
admin.site.register(Promoteur)
admin.site.register(Groupe)
admin.site.register(Stagier)
admin.site.register(TypeStage)
admin.site.register(Stage)

