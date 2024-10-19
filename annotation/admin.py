from django.contrib import admin
from .models import Coordinates, Location

admin.site.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'removed')
    search_fields = ('latitude', 'longitude')
    list_filter = ('removed',)


admin.site.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('accessibility_score', 'adjacent_street', 'removed')
    search_fields = ('accessibility_score', 'adjacent_street',)
    list_filter = ('removed',)