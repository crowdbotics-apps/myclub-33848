from django.contrib import admin
from .models import Articles, Evenements, Listecategorie, Listerole, Rencontres, Tests

admin.site.register(Listecategorie)
admin.site.register(Listerole)
admin.site.register(Articles)
admin.site.register(Evenements)
admin.site.register(Rencontres)
admin.site.register(Tests)

# Register your models here.
