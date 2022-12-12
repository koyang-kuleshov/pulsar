from django.urls import path

from .views import GetProducts, get_product


urlspatterns = [
    path('products', GetProducts.as_view(), 'get-products'),
    path('get/product/pk:int', get_product, 'get-product'),

]
