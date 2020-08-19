from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactForm, UserProfiles


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','subject','status']
    list_filter = ['status']

class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'image_tag',]


admin.site.register(Setting)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(UserProfiles, UserProfilesAdmin)
