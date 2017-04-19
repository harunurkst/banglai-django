from django.contrib import admin
from information.models import Divisions, Districts


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','division', 'visited', 'population_density')

admin.site.register(Divisions)
admin.site.register(Districts, DistrictAdmin)
