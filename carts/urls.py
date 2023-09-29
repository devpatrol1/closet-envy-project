from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart_qty/<int:product_id>/', views.add_cart_qty, name='add_cart_qty'),
    path('subtract_cart_qty/<int:product_id>/<int:cart_item_id>/', views.subtract_cart_qty, name='subtract_cart_qty'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
]
