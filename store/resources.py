from .models import Product, Variation
from import_export import resources


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class VariationResource(resources.ModelResource):
    class Meta:
        model = Variation

