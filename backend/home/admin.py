from django.contrib import admin
from .models import Articles, Listecategorie, Listerole

admin.site.register(Listecategorie)
admin.site.register(Listerole)
admin.site.register(Articles)

# Register your models here.
