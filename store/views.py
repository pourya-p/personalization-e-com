from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from .forms import PersonalizeForm
from .models import Product


class IndexView(View):
    form_class = PersonalizeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'store/index.html', {'form': form})


class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter(
            sex=request.GET.get('sex', None),
            age_max__gte=request.GET.get('age', None),
            age_min__lte=request.GET.get('age', None),
            height_max__gte=request.GET.get('height', None),
            height_min__lte=request.GET.get('height', None),
            weight_max__gte=request.GET.get('weight', None),
            weight_min__lte=request.GET.get('weight', None),

        )
        return render(request, 'store/product_list.html', {'products': products})

