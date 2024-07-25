from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import PersonalizeForm
from .models import Product


class IndexView(View):
    form_class = PersonalizeForm

    def get(self, request, errors=None):
        return render(request, 'store/index.html', {'errors': errors})


class ProductListView(View):
    form_class = PersonalizeForm
    def get(self, request):
        form = self.form_class(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            products = Product.objects.filter(
                sex=cd['sex'],
                age_max__gte=cd['age'],
                age_min__lte=cd['age'],
                height_max__gte=cd['height'],
                height_min__lte=cd['height'],
                weight_max__gte=cd['weight'],
                weight_min__lte=cd['weight'],

            )
            return render(request, 'store/product_list.html', {'products': products})
        else:

            return IndexView().get(request, form.errors)


class ProductDetail(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'store/product_detail.html', {'product': product})
