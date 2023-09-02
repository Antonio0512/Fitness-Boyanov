from django.contrib import admin
from .models import Photo, Gallery


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("caption",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)
