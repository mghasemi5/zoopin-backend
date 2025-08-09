from django import forms
from api.models import Partner
from api.models import InfoBlock,logos,insights,testimonials,slider

class InfoBlockForm(forms.ModelForm):
    class Meta:
        model = InfoBlock
        fields = '__all__'


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

class logoForm(forms.ModelForm):
    class Meta:
        model = logos
        fields = '__all__'

class insightForm(forms.ModelForm):
    class Meta:
        model = insights
        fields = '__all__'

class testimonialForm(forms.ModelForm):
    class Meta:
        model = testimonials
        fields = '__all__'

class sliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = '__all__'