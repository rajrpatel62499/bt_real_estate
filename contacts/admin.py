from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "listing", "phone", "email", "contact_date")
    list_display_links = ("id", "name", "listing")
    search_fields = ("name", "phone", "email", "listing")
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
