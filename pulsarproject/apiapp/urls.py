from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import CreateProduct, GetProduct, ListProducts, main


schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Products API for Pulsar",
      contact=openapi.Contact(email="michel@koyang-kuleshov.ru"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('health-check/', main, name='health-check'),
    path('products/', ListProducts.as_view(), name='list-products'),
    path('get/product/<int:pk>', GetProduct.as_view(), name='get-product'),
    path('create/product/', CreateProduct.as_view(), name='create-product'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]
