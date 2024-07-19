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
    )

    age = forms.IntegerField(label='سن')

    height = forms.IntegerField(label='قد')

    weight = forms.IntegerField(label='وزن')

    def clean_age(self):
        age = self.cleaned_data['age']
        if settings.MIN_PRODUCT_AGE < age <= settings.MAX_PRODUCT_AGE:
            raise ValidationError('حداقل سن مجاز 13 می باشد')
        return age

    def clean_height(self):
        height = self.cleaned_data['height']
        if settings.MIN_PRODUCT_HEIGHT < height <= settings.MAX_PRODUCT_HEIGHT:
            raise ValidationError('حداقل قد مجاز 100 می باشد')
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if settings.MIN_PRODUCT_WEIGHT < weight <= settings.MAX_PRODUCT_WEIGHT:
            raise ValidationError('حداقل وزن مجاز 30 می باشد')
        return weight
