from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    img = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    description = models.TextField()
    sex = models.CharField(
        choices=(
            ('0', 'زن'),
            ('1', 'مرد'),
        ),
        max_length=1,
    )
    age_min = models.PositiveIntegerField(default=0)
    age_max = models.PositiveIntegerField(default=0)
    height_min = models.PositiveIntegerField(default=0)
    height_max = models.PositiveIntegerField(default=0)
    weight_min = models.PositiveIntegerField(default=0)
    weigh_max = models.PositiveIntegerField(default=0)
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.name