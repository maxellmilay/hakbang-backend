from django.contrib import admin
from .models import CustomUser, Organization


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_staff', 'is_active', 'organization', 'date_joined')
    search_fields = ('username', 'email', 'organization__name')
    list_filter = ('is_admin', 'is_staff', 'is_active', 'organization', 'date_joined')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'password')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'username', 'email', 'password')
        }),
        ('Profile Picture', {
            'fields': ('profile_picture',)  # You already have a foreign key for profile_picture in CustomUser
        }),
        ('Organization', {
            'fields': ('organization',)
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_superuser', 'is_staff', 'is_active')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('password',)
        return self.readonly_fields

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'removed')
    search_fields = ('name',)
    list_filter = ('removed',)
    ordering = ('-created_on',)
    readonly_fields = ('created_on',)

    fieldsets = (
        (None, {
            'fields': ('name', 'profile_picture')
        }),
        ('Status', {
            'fields': ('removed',)
        }),
        ('Important Dates', {
            'fields': ('created_on',)
        }),
    )
