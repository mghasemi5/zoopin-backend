from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet, InfoBlockViewSet, logosViewSet, insightViewSet, testimonialsViewSet, sliderViewSet, \
    AboutPageViewSet, ServiceViewSet

router = DefaultRouter()
router.register(r'partners', PartnerViewSet)
router.register(r'info-blocks', InfoBlockViewSet)
router.register(r'logos', logosViewSet)
router.register(r'insights', insightViewSet)
router.register(r'testimonials', testimonialsViewSet)
router.register(r'slider', sliderViewSet)
router.register(r'about', AboutPageViewSet)
router.register(r"services", ServiceViewSet, basename="services")
urlpatterns = [
    path('', include(router.urls)),
]
