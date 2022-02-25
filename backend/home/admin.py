from django.contrib import admin
from .models import Listecategorie, Listerole, Utilisateurs

admin.site.register(Utilisateurs)
admin.site.register(Listecategorie)
admin.site.register(Listerole)

# Register your models here.
