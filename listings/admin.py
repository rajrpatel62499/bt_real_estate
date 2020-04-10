from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "state","is_published", "list_date", "realtor")
    list_display_links = ("id", "title")
    list_editable = ("is_published","state","price")
    list_per_page = 10
    list_filter = ("realtor",)
    search_fields = ("zipcode", "title", "city", "state", "description", "price")


admin.site.register(Listing, ListingAdmin)
