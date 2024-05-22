from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('products_category/', CategoryView.as_view(), name='products-category'),
    path('football/', ProductView.as_view(), name='football'),
    path('order_create/', OrderView.as_view(), name='order-create'),
    path('order_detail/<int:pk>/', OrderSuccessView.as_view(), name='order-detail'),
    path('order/', OrderView.as_view(), name='order-form'),
    path('order_success/', OrderSuccessView.as_view(), name='order-success'),
    path('basketball/', BasketballView.as_view(), name='basketball'),
    path('mma/', MMAView.as_view(), name='mma'),
]