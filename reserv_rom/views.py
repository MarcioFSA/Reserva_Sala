from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'Reserva':'  Sala de Treinamento'
    }
    return render(request, 'index.html')

def reserva(request):
    return render(request, 'reserva.html')

