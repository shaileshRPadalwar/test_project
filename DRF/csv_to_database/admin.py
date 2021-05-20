from django.contrib import admin
from .models import Csv_date
# Register your models here.

class Csv_dateAdmin(admin.ModelAdmin):
    list_display=['date']

admin.site.register(Csv_date,Csv_dateAdmin)