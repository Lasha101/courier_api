from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()

router.register(r'users', CustomUserViewSet)
router.register(r'parcels', ParcelViewSet)
router.register(r'delivery_proof', DeliveryProofViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]



