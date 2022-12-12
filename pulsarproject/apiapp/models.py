from django.db import models


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
    INSTOCK = 'in_stock'
    ONREQUEST = 'on_request'
    EXPECTED = 'expected'
    OUTOFSTOCK = 'out_of_stock'
    NOTPRODUCE = 'not_produce'
    CHOICES = [
        (INSTOCK, 'В наличии'),
        (ONREQUEST, 'Под заказ'),
        (EXPECTED, 'Ожидается поступление'),
        (OUTOFSTOCK, 'Нет в наличии'),
        (NOTPRODUCE, 'Не производится'),
    ]
    status = models.CharField(
                              max_length=32,
                              choices=CHOICES,
                              default=INSTOCK,
                              )
    image = models.ImageField('image')

    def __str__(self):
        return self.name
