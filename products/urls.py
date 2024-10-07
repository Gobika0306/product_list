from django.urls import path
from .views import RegisterAPIView, LoginAPIView, product_list  # Use the correct view names

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('products/', product_list, name='product-list'),
]
