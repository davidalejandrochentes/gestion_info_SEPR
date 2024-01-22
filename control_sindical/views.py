from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Sindicato, Trabajador, Map, AsambleaAfiliados


# Create your views here.
@login_required
def index(request):
    return render(request, 'control_sindical/index.html', {})

def log_in(request):
    if request.method =='GET':
        return render(request, 'control_sindical/login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, "El usuario no existe, o la password es incorrecta")
            return render(request, 'control_sindical/login.html', {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('index')
        
@login_required
def log_out(request):
    logout(request)
    return redirect('index')  

@login_required
def sindicato(request):
    sindicatos = Sindicato.objects.filter(nombre__icontains=request.GET.get('search', ''))
    cantidad = len(sindicatos)
    context = {
        'sindicatos': sindicatos,
        'cantidad': cantidad,
    }
    return render(request, 'control_sindical/sindicatos.html', context)

@login_required
def datos_sindicato(request, id):
    sindicato = get_object_or_404(Sindicato, id=id)
    trabajadores = Trabajador.objects.filter(nombre__icontains=request.GET.get('search', ''), sindicato=sindicato)
    context = {
        'sindicato': sindicato,
        'trabajadores': trabajadores,
    }
    return render(request, 'control_sindical/datos_sindicatos.html', context)


@login_required
def detalles_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    context = {
        'trabajador': trabajador
    }
    return render(request, 'control_sindical/detalles_trabajador.html', context)

@login_required
def trabajadores(request):
    trabajadores = Trabajador.objects.filter(nombre__icontains=request.GET.get('search', ''))
    context = {
        'trabajadores': trabajadores,
    }
    return render(request, 'control_sindical/trabajadores.html', context)

@login_required
def mapt(request):
    trabajadores = Trabajador.objects.filter(nombre__icontains=request.GET.get('search', ''))
    context = {
        'trabajadores': trabajadores,
    }
    return render(request, 'control_sindical/map.html', context)

@login_required
def asambleas(request):
    nombre_sindicato = request.GET.get('search', '')
    asambleas = AsambleaAfiliados.objects.filter(sindicato__nombre__icontains=nombre_sindicato).order_by('-fecha')
    context = {
        'asambleas': asambleas,
    }
    return render(request, 'control_sindical/asambleas.html', context)