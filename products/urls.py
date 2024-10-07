from django.urls import path
from .views import RegisterAPIView, LoginAPIView, product_list  

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('products/', product_list, name='product-list'),
]
