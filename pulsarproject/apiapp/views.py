from rest_framework import generics

from .models import Product
from .serializers import ListProductSerializer, ProductSerializer


class GetProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        return (
            super(*args, **kwargs)
            .get_queryset()
            .filter(pk=self.kwargs.get("pk"))
        )


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(*args, **kwargs).get_queryset()
        if self.request.GET.get("sku"):
            queryset = queryset.filter(sku=self.request.GET["sku"])
        elif self.request.GET.get("name"):
            queryset = queryset.filter(name=self.request.GET["name"])
        if self.request.GET.get("filter"):
            queryset = queryset.filter(status=self.request.GET["filter"])
        return queryset


class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
