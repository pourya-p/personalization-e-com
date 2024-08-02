from django.contrib import admin
from .models import OrderProduct, Order

class ProductOrderInLine(admin.StackedInline):
    model = OrderProduct
    raw_id_fields = ['product']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInLine]


admin.site.register(Order, OrderAdmin)
