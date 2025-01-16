from django.contrib import admin
from .models import File, Coordinates, Sidewalk, AnnotationForm, Annotation, AnnotationImage

class AnnotationImageInline(admin.TabularInline):
    model = AnnotationImage
    extra = 1
    raw_id_fields = ('file',)

class AnnotationInline(admin.StackedInline):
    model = Annotation
    extra = 0
    raw_id_fields = ('annotator', 'template', 'coordinates')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_on', 'removed')
    list_filter = ('removed', 'created_on')
    search_fields = ('url',)
    date_hierarchy = 'created_on'

@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'removed')
    list_filter = ('removed',)
    search_fields = ('latitude', 'longitude')

@admin.register(Sidewalk)
class SidewalkAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'accessibility_score', 'adjacent_street', 'removed')
    list_filter = ('removed', 'accessibility_score')
    search_fields = ('adjacent_street', 'data')
    raw_id_fields = ('start_coordinates', 'end_coordinates')
    inlines = [AnnotationInline]

    def get_name(self, obj):
        return str(obj)
    get_name.short_description = 'Name'

@admin.register(AnnotationForm)
class AnnotationFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'updated_on', 'removed')
    list_filter = ('removed', 'created_on', 'updated_on')
    search_fields = ('name',)
    date_hierarchy = 'updated_on'

@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('name', 'sidewalk', 'annotator', 'created_on', 'updated_on', 'removed')
    list_filter = ('removed', 'created_on', 'updated_on')
    search_fields = ('name', 'annotator__username', 'sidewalk__adjacent_street')
    raw_id_fields = ('sidewalk', 'annotator', 'template', 'coordinates')
    date_hierarchy = 'updated_on'
    inlines = [AnnotationImageInline]

@admin.register(AnnotationImage)
class AnnotationImageAdmin(admin.ModelAdmin):
    list_display = ('get_file_url', 'get_annotation_name')
    raw_id_fields = ('file', 'annotation')

    def get_file_url(self, obj):
        return obj.file.url
    get_file_url.short_description = 'File URL'

    def get_annotation_name(self, obj):
        return obj.annotation.name
    get_annotation_name.short_description = 'Annotation Name'
