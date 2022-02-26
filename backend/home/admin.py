from django.contrib import admin
from .models import Articles, Evenements, Listecategorie, Listerole

admin.site.register(Listecategorie)
admin.site.register(Listerole)
admin.site.register(Articles)
admin.site.register(Evenements)

# Register your models here.
