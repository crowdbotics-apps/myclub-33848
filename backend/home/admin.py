from django.contrib import admin
from .models import Articles, Evenements, Listecategorie, Listerole, Rencontres

admin.site.register(Listecategorie)
admin.site.register(Listerole)
admin.site.register(Articles)
admin.site.register(Evenements)
admin.site.register(Rencontres)

# Register your models here.
