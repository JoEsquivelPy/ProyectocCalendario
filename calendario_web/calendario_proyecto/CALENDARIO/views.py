from django.shortcuts import render
from modelo import Evento
# Create your views here.

def calendario(request):
    eventos = Evento.objects.all()
    return render(request, 'calendario/calendario.html', {'eventos': eventos})
