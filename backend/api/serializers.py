from rest_framework import serializers
from .models import Partner, Service
from .models import InfoBlock,logos,insights,testimonials,slider,AboutPage

class InfoBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBlock
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class logosSerializer(serializers.ModelSerializer):
    class Meta:
        model = logos
        fields = '__all__'

class insightSerializer(serializers.ModelSerializer):
    class Meta:
        model = insights
        fields = '__all__'
class testimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = testimonials
        fields = '__all__'
class sliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = slider
        fields = '__all__'
class AboutPageSerializer(serializers.ModelSerializer):
    hero_image = serializers.SerializerMethodField()

    def get_hero_image(self, obj):
        return obj.hero_image.url if obj.hero_image else ""

    class Meta:
        model = AboutPage
        fields = ["title","tagline","body","body_is_html","hero_image","highlights","contact","seo","updated_at"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "slug", "description", "image"]