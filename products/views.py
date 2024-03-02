from rest_framework import viewsets
from products.models import Product
from products.serliazers import ProductSerlizers


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerlizers
    queryset = Product.objects.all()
