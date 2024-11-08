from django.urls import path
from .views import *


urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('create_order/', create_order, name='create_order'),
    path('order/', order, name='order'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
]