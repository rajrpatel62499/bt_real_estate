from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', 'is_mvp', 'phone', 'photo')
    list_display_links = ('id','name')
    list_editable = ['is_mvp', 'phone']
    list_per_page = 10

admin.site.register(Realtor, RealtorAdmin)