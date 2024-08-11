from django.shortcuts import render, redirect

from mysite.base.forms import LoginForm, EsqueciSenha


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'base/index.html', {'form': form})
        form.save()
        return redirect('base:login')
    form = LoginForm()
    return render(request, 'base/index.html', {'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'base/login.html', {'form': form})


def esqueci(request):
    if request.method == 'POST':
        form = EsqueciSenha(request.POST)
        if not form.is_valid():
            return render(request, 'base/esqueci.html', {'form': form})
        return redirect('base:senha_enviada')
    form = EsqueciSenha()
    return render(request, 'base/esqueci.html', {'form': form})


def senha_enviada(request):
    form = LoginForm()
    return render(request, 'base/senha_enviada.html', {'form': form})
