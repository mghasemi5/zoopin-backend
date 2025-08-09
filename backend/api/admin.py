from django.contrib import admin
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'email', 'website', 'phone')
    search_fields = ('name', 'email', 'website')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'tagline', 'description', 'bio')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'website', 'link')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
