from django.shortcuts import render
# Libreria de django con formulario de creacion de usuario
from django.contrib.auth.forms import UserCreationForm
# Genera un modelo de usuario automatico a traves de POST
from django.contrib.auth.models import User
from django.http import HttpResponse
# from http.client import HTTPResponse


# Views.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register User TODO: MINUTO 34:45 VIDEO
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
