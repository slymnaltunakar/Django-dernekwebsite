from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Category, Product, Images

class ProductImageInLine(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'category', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['category']
    inlines = [ProductImageInLine]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'icerik', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)