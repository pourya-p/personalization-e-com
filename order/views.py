from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .forms import OrderForm
from .models import Order, OrderProduct
from basket.basket import Basket

class CheckoutView(View):
    form_class = OrderForm

    def get(self, request):
        if request.session.get('basket'):
            return render(request, 'order/checkout.html', {'form':self.form_class()})
        else:
            return redirect('store:index')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            basket = Basket(request)
            cd = form.cleaned_data
            order = Order.objects.create(
                name=cd['name'],
                phone_number=cd['phone_number'],
                address=cd['address'],
                total_price=basket.total_price(),
            )

            for item in basket:
                order_product = OrderProduct.objects.create(
                    order=order,
                    product=item['product'],
                    qty=item['qty'],
                    price_on_order=item['total_price'],
                )
            del request.session['basket']
            return render(request, 'order/result.html')
        return render(request, 'order/checkout.html', {'form': form})
