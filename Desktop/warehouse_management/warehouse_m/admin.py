from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('category', 'product', 'price')
    list_filter = ('category', 'manufacturer')
    search_fields = ('category', 'product', 'code')





