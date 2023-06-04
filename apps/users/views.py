from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages



# Create your views here.
def register(request):
    data ={
        'form' : CustomUserCreationForm()
    }

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to='home')
        else:
            data['form'] = form


    return render(request, "registration/register.html", data)