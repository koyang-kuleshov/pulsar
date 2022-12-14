import logging as log
import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image


class Product(models.Model):
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name']
        indexes = [
                   models.Index(fields=['name', 'sku', 'status']),
                   ]

    name = models.CharField('name', max_length=255)
    sku = models.CharField('sku', max_length=255, unique=True)
    price = models.DecimalField('price',  max_digits=10, decimal_places=2)
    IN_STOCK = 'in_stock'
    ON_REQUEST = 'on_request'
    EXPECTED = 'expected'
    OUT_OFSTOCK = 'out_of_stock'
    NOT_PRODUCE = 'not_produce'
    CHOICES = [
        (IN_STOCK, 'В наличии'),
        (ON_REQUEST, 'Под заказ'),
        (EXPECTED, 'Ожидается поступление'),
        (OUT_OFSTOCK, 'Нет в наличии'),
        (NOT_PRODUCE, 'Не производится'),
    ]
    status = models.CharField(
                              max_length=32,
                              choices=CHOICES,
                              default=IN_STOCK,
                              )
    image = models.ImageField('image', upload_to="images")

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def convert_to_webp(sender, instance, **kwargs):
    path = instance.image.path
    try:
        image = Image.open(path)
    except OSError as er:
        log.error(f"Error while opening file: {er}")
        raise er
    image.convert("RGB")
    path, filename = os.path.split(path)
    filename = filename.split(".")[0]
    filename = f"{filename}.webp"
    image.save(os.path.join(path, filename), "webp")
