from django.shortcuts import render, redirect

from mysite.base.forms import LoginForm


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            print("Form is not valid:", form.errors)
            return render(request, 'base/index.html', {'form': form})
        print("Form is valid, redirecting...")
        return redirect('base/origin.html')
    form = LoginForm()
    return render(request, 'base/index.html', {'form': form})
