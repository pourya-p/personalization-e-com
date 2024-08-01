from django.shortcuts import render
from django.views import View
from .forms import OrderForm

class CheckoutView(View):
    form_class = OrderForm
    def get(self, request):
        return render(request, 'order/checkout.html')

    def post(self, request):
        pass