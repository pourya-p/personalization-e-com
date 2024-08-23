from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .basket import Basket
from store.models import Product



class BasketSummeryView(TemplateView):
    template_name = "basket/basket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'personal' in self.request.session:
            context['personal'] = self.request.session['personal']
        return context

class AddToBasketView(View):
    def post(self, request):
        basket = Basket(request)
        product = get_object_or_404(Product, id=request.POST['product_id'])
        basket.add(product, 1)
        response = JsonResponse({'msg': 'به سبد خرید اضافه شد'}, status=201)
        return response
