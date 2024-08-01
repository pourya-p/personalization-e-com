from django.urls import path, re_path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product-list', views.ProductListView.as_view(), name='product_list'),
    re_path(r'product/(?P<slug>[-\w]+)', views.ProductDetail.as_view(), name='product_detail'),

]
