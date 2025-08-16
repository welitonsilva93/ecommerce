
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app_loja.views import ProdutosViewSet


router = routers.DefaultRouter()
router.register(r'produtos', ProdutosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_loja.urls')),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
