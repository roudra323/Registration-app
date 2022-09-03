from django.shortcuts import render
from .forms import formdata
from .models import User
# Create your views here.


def regi(request):
    if request.method == 'POST':
        form = formdata(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            p = form.cleaned_data['psrd']
            reg = User(name=nm, email=em, password=p)
            reg.save()
            return render(request, 'register/success.html', {'name': nm})

    else:
        form = formdata()

    return render(request, 'register/regi.html', {'form': form})
