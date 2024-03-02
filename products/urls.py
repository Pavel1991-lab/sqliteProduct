from products.apps import ProductsConfig
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

app_name = ProductsConfig.name

router = DefaultRouter()


router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [

] + router.urls