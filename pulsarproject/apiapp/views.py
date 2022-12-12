from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view
def get_product():
    ...


class GetProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
