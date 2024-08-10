from django import forms


class LoginForm(forms.Form):
    nome = forms.CharField(
        label='nome',
        max_length=64,
        min_length=3,
        required=True,
    )
    email = forms.EmailField(
        label='email',
        required=True,
    )
    senha = forms.CharField(
        label='senha',
        max_length=64,
        min_length=3,
        required=True,
        widget=forms.PasswordInput,
    )
    idade = forms.IntegerField(
        label='idade',
    )
