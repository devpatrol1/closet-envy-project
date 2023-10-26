from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
from .resources import VariationResource, ProductResource
from import_export.admin import ImportExportModelAdmin
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VariationResource
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
