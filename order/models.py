from django.db import models
from store.models import Product


class Order(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='نام')
    phone_number = models.CharField(max_length=11, blank=False, null=True, verbose_name='تلفن')
    address = models.CharField(max_length=500, blank=False, null=True, verbose_name='آدرس')
    total_price = models.PositiveIntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)


def get_sentinel_product():
    return Product.objects.get_or_create(name="deleted")[0]


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET(get_sentinel_product))
    qty = models.PositiveSmallIntegerField()
    price_on_order = models.PositiveIntegerField()

