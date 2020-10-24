from django.contrib import admin

from webapp.models import Photo, Favorites


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'image', 'signature', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['signature', 'created_at']
    fields = ['image', 'signature', 'created_at', 'author']
    readonly_fields = ['created_at']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favorites)