from django.views.generic import ListView
from django.db.models import Q
from store.models import Product


class SearchView(ListView):
    model = Product
    paginate_by = 6
    page_kwarg = 'page'
    template_name = 'store/product_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')

        return Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))