from django.urls import path, re_path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'/product/(?P<slug>[-\w]+)', views.IndexView.as_view(), name='index'),

]