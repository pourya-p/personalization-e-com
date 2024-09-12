from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View
from django.views.generic import ListView, FormView
from django.core.paginator import Paginator
from .forms import PersonalizeForm
from .models import Product, Category


class IndexFormView(FormView):
    template_name = 'store/index.html'
    form_class = PersonalizeForm

    def get_success_url(self):
        form_data = self.request.POST
        sex = form_data['sex']
        age = form_data['age']
        height = form_data['height']
        weight = form_data['weight']
        url = f'product-list?sex={sex}&age={age}&height={height}&weight={weight}'
        return url


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    page_kwarg = 'page'
    template_name = 'store/product_list.html'


    def get_queryset(self):
        if category_slug := self.kwargs.get('category'):
            category = get_object_or_404(Category, slug=category_slug)
            products = category.products.all()
            return products
        if self.request.GET.get('sex'):
            q = self.request.GET
            return get_list_or_404(
                Product,
                sex=q['sex'],
                age_max__gte=q['age'],
                age_min__lte=q['age'],
                height_max__gte=q['height'],
                height_min__lte=q['height'],
                weight_max__gte=q['weight'],
                weight_min__lte=q['weight'],

            )
        return super().get_queryset()


class ProductDetail(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'store/product_detail.html', {'product': product})
