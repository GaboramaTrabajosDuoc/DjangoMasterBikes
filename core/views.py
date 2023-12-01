from django.shortcuts import redirect, render
from .forms import RepSolic, RepairForm
from django.http import HttpResponseRedirect
from .models import RepSolic
from django.contrib import messages



# Create your views here.

def index (request):

    return render(request,'core/index.html')


def arbici (request):

    return render(request,'core/arrriendobicis.html')

def repa (request):
    submitted = False
    if request.method =="POST":
            form = RepairForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/Reparaciones?submitted=True')
    else:
        form = RepairForm
        if 'submitted' in request.GET:
            submitted= True
    return render(request,'core/Reparacionbicis.html',{'form':form, 'submitted':submitted})    

def us (request):

    return render(request,'core/nosotros.html')

def prod (request):

    return render(request,'core/productos.html')


def job (request):
    job_list = RepSolic.objects.all()
    us = request.user
    #breakpoint() == puntos de pausa para revisar como avanza el codigo
    #Revisar consola y apretar help para solicitar ayuda al 911
    if us.username == "admin" or us.username == "Tecnico":
        return render(request,'core/vista_tecnico.html',
        {'job_list': job_list})
    else:
        messages.success(request, ("No cuentas con permisos para acceder a esta seccion 🔒"))        
        return render(request,'core/index.html')



def delete_RepSolic(request,Nombre):
    solic = RepSolic.objects.get(Nombre=Nombre)
    solic.delete()
    return redirect(job)


# def delete_RepSolic(request, RepSolic_id):
# 	event = RepSolic.objects.get(pk=RepSolic_id)
# 	if request.user == RepSolic.Tecnico:
# 		RepSolic.delete()
# 		messages.success(request, ("Borrado!!"))
# 		return redirect('Vista tecnico')		
# 	else:
# 		messages.success(request, ("No tienes permiso"))
# 		return redirect('Vista tecnico')	