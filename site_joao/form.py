from django.forms import ModelForm
from site_joao.models import *
from django import forms

class Form_Register(ModelForm):
    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(Form_Register, self).__init__(*args, **kwargs)

    class Meta():
        model = Usuario
        fields = '__all__'
        exclude = ['superAdm', 'moderador']
        widgets = {
            'password': forms.PasswordInput(),
        }


class FormConteudo(ModelForm):
    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormConteudo, self).__init__(*args, **kwargs)

    class Meta():
        model = Conteudo
        exclude = ['imagem', 'status']



