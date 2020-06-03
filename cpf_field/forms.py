from django.forms import ModelForm
from cpf_field.models import MyModel


class CPFFieldForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['cpf']
