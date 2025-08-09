from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Partner
from .serializers import PartnerSerializer
from .models import InfoBlock,logos,insights,testimonials,slider
from .serializers import InfoBlockSerializer,logosSerializer,insightSerializer,testimonialsSerializer,sliderSerializer

class InfoBlockViewSet(viewsets.ModelViewSet):
    queryset = InfoBlock.objects.all()
    serializer_class = InfoBlockSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slug']

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class logosViewSet(viewsets.ModelViewSet):
    queryset = logos.objects.all()
    serializer_class = logosSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class insightViewSet(viewsets.ModelViewSet):
    queryset = insights.objects.all()
    serializer_class = insightSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class testimonialsViewSet(viewsets.ModelViewSet):
    queryset = testimonials.objects.all()
    serializer_class = testimonialsSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class sliderViewSet(viewsets.ModelViewSet):
    queryset = slider.objects.all()
    serializer_class = sliderSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]