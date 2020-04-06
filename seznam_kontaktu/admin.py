from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'phone_number', 'email',)

admin.site.register(Contact, ContactAdmin)