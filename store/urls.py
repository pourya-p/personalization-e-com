from django.urls import path, re_path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.IndexFormView.as_view(), name='p_search'),
    path('product-list', views.ProductListView.as_view(), name='product_list'),
    re_path('product-list/(?P<category>[-\w]+)', views.ProductListView.as_view(), name='product_list_cat'),
    re_path(r'product/(?P<slug>[-\w]+)', views.ProductDetail.as_view(), name='product_detail'),
]
