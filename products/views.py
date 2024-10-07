from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
import requests
from django.http import JsonResponse



# Register API
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Login API
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)



def product_list(request):
    if request.method == 'GET':
        response = requests.get('https://dummyapi.online/api/products')
        if response.status_code == 200:
            products = response.json()
            return JsonResponse(products, safe=False)  # Return the products as JSON
        return JsonResponse({"error": "Unable to fetch products"}, status=500)
    return JsonResponse({"error": "Method not allowed"}, status=405)
