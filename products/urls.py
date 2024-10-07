from django.urls import path
from .views import RegisterAPI, LoginAPI, product_list

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('products/', product_list, name='product_list'),
]
