from django import forms
from .models import Country, Image

class CountryWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryWriteForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = '나라'

    class Meta:
        model = Country
        fields = ['country',]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image',]