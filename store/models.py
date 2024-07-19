from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    img = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    description = models.TextField()
    sex = models.CharField(
        choices=(
            ('0', 'زن'),
            ('1', 'مرد'),
        ),
        max_length=1,
    )
    age_min = models.PositiveIntegerField(default=settings.MIN_PRODUCT_AGE, validators=[MinValueValidator(settings.MIN_PRODUCT_AGE)])
    age_max = models.PositiveIntegerField(default=settings.MAX_PRODUCT_AGE, validators=[MaxValueValidator(settings.MAX_PRODUCT_AGE)])
    height_min = models.PositiveIntegerField(default=settings.MIN_PRODUCT_HEIGHT, validators=[MinValueValidator(settings.MIN_PRODUCT_HEIGHT)])
    height_max = models.PositiveIntegerField(default=settings.MAX_PRODUCT_HEIGHT, validators=[MaxValueValidator(settings.MAX_PRODUCT_HEIGHT)])
    weight_min = models.PositiveIntegerField(default=settings.MIN_PRODUCT_WEIGHT, validators=[MinValueValidator(settings.MIN_PRODUCT_WEIGHT)])
    weight_max = models.PositiveIntegerField(default=settings.MAX_PRODUCT_WEIGHT, validators=[MaxValueValidator(settings.MAX_PRODUCT_WEIGHT)])
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.name