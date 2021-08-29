from django.contrib import admin
from.models import Gallery, nutritionGuides

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
    )


class nutritionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(nutritionGuides, nutritionAdmin)