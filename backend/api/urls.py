from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, InfoBlockViewSet,logosViewSet,insightViewSet,testimonialsViewSet,sliderViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'info-blocks', InfoBlockViewSet)
router.register(r'logos', logosViewSet)
router.register(r'insights', insightViewSet)
router.register(r'testimonials', testimonialsViewSet)
router.register(r'slider', sliderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
