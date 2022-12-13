from django.urls import path, re_path

from .views import CreateProduct, ListProducts, GetProduct


urlpatterns = [
    path('products', ListProducts.as_view(), name='list-products'),
    # re_path((r'^products(?:name=(?P<name>\w+))&'
    #          r'(?:sku=(?P<sku>\w+))&(?:filter=(?P<filter>\w+))?$'),
    #         ListProducts.as_view(),
    #         name='list-products'),
    path('get/product/<int:pk>', GetProduct.as_view(), name='get-product'),
    path('create/product/', CreateProduct.as_view(), name='create-product'),
]
