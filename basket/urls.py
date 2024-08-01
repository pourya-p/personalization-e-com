from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.BasketSummeryView.as_view(), name='basket_summery'),
    path('add', views.AddToBasketView.as_view(), name='add_to_basket'),
]
