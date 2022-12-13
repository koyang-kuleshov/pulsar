import os
from rest_framework import serializers

from .models import Product


class ListProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product


class ProductSerializer(serializers.Serializer):
    class Meta:
        fields = "__all__"
        model = Product

    class ImageCustomField(serializers.Field):

        def to_representation(self, value):
            slug = -3
            path_and_file = 0
            path = value.path
            _, filename = os.path.split(path)
            path = os.path.join(*path.split("/")[slug:])
            path = path.split(".")[path_and_file]
            extension = filename.split(".")[1].lower()
            return {
                "path": path,
                "formats": [extension, "webp"]
                }

        def to_internal_value(self, data):
            ...

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    sku = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField(max_length=32)
    image = ImageCustomField()
