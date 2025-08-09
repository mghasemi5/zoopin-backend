from rest_framework import serializers
from .models import Partner
from .models import InfoBlock,logos,insights,testimonials,slider

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

