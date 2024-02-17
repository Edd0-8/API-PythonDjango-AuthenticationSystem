from django.shortcuts import render

# Libreria de django con formulario de creacion de usuario
from django.contrib.auth.forms import UserCreationForm


# Views.
def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })