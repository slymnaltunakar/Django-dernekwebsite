from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from icerik.models import CImages, Icerik


class IcerikImageInline(admin.TabularInline):
    model = CImages
    extra = 3


class ContentAdmin(admin.ModelAdmin):
    list_display=['title','type','image_tag','status','create_at']
    list_filter = ['status','type']
    inlines = [IcerikImageInline]
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Icerik,ContentAdmin)