from django import forms
from django.core.exceptions import ValidationError
from django.conf import settings


class PersonalizeForm(forms.Form):
    sex = forms.ChoiceField(
        choices=(
            ('0', 'زن'),
            ('1', 'مرد'),
        ),
        label='جنسیت',
        widget=forms.Select(
            attrs={
                'placeholder': 'Name', 'style': 'text-align-last:center;', 'class': 'form-control'
            }
        )
    )

    age = forms.IntegerField(label='سن', widget=forms.NumberInput(attrs={'placeholder': 'سن', 'class':'form-control'}))

    height = forms.IntegerField(label='قد', widget=forms.NumberInput(attrs={'placeholder': 'قد', 'class':'form-control'}))

    weight = forms.IntegerField(label='وزن', widget=forms.NumberInput(attrs={'placeholder': 'وزن', 'class':'form-control'}))

    def clean_age(self):
        age = self.cleaned_data['age']
        if not (settings.MIN_PRODUCT_AGE < age <= settings.MAX_PRODUCT_AGE):
            raise ValidationError('حداقل سن مجاز 13 می باشد')
        return age

    def clean_height(self):
        height = self.cleaned_data['height']
        if not (settings.MIN_PRODUCT_HEIGHT < height <= settings.MAX_PRODUCT_HEIGHT):
            raise ValidationError('حداقل قد مجاز 100 می باشد')
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if not (settings.MIN_PRODUCT_WEIGHT < weight <= settings.MAX_PRODUCT_WEIGHT):
            raise ValidationError('حداقل وزن مجاز 30 می باشد')
        return weight
