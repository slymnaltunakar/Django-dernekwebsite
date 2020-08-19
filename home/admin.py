from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactForm, UserProfili


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']

class UserProfiliAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'city', 'country', 'image_tag']


admin.site.register(Setting)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(UserProfili, UserProfiliAdmin)

