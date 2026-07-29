from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["category", "condition"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "name", "created_at"]
