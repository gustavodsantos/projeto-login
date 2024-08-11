from django import forms
from mysite.base.models import Cadastro


class LoginForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail', 'required': True}),
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'required': True, 'minlength': 8}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Digite sua idade'}),
        }


class EsqueciSenha(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form', 'placeholder': 'Digite seu e-mail'})
    )
