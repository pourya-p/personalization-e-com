from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .basket import Basket
from store.models import Product



class BasketSummeryView(TemplateView):
    template_name = "basket/basket.html"


class AddToBasketView(View):
    def post(self, request):
        basket = Basket(request)
        product = get_object_or_404(Product, id=request.POST['product_id'])
        basket.add(product, 1)
        response = JsonResponse({'msg': 'به سبد خرید اضافه شد'}, status=201)
        return response
