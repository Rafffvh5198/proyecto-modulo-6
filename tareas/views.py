from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required #evitar visitas no deseadas
from .models import Proyecto, Tarea
from .forms import ProyectoForm,TareaForm,RegistroForm
# Create your views here.

@login_required #seguridad
def lista_proyectos(request):
    proyectos=Proyecto.objects.filter(usuario=request.user) #cambiamos all por filter muestra proyectos de usuario logueado
    
    return render(request,'proyectos.html',{'proyectos':proyectos})
@login_required
def crear_proyecto(request):
    if request.method== "POST":
        form=ProyectoForm(request.POST)
        
        if form.is_valid():                        #verificando si el formulario es valido
            proyecto=form.save(commit=False)       #si lo es, se guarda y se asigna un usuario y redirijimos
            proyecto.usuario =request.user
            proyecto.save() 
            
            return redirect('proyectos')
        
    else:                                          #si el metodo no es post retornamos el formulario sin info
        form=ProyectoForm()
    return render(request,'crear_proyecto.html',{'form':form})

@login_required
def crear_tarea(request,proyecto_id):              #como la tarea esta asociado a un proyecto se debe validar el proyecto
    
    proyecto=get_object_or_404(Proyecto,id=proyecto_id, usuario=request.user)   #con esto verificamos q efectivamente el proyecto pertenezca al usuario
    
    if request.method== "POST":
        form=TareaForm(request.POST)
        
        if form.is_valid():                        #verificando si el formulario es valido
            tarea=form.save(commit=False)       #si lo es, se guarda y se asigna un usuario y redirijimos
            tarea.proyecto =proyecto
            tarea.save() 
            
            return redirect('proyectos')
        
    else:                                          #si el metodo no es post retornamos el formulario sin info
        form=TareaForm()
    return render(request,'crear_tarea.html',{'form':form,'proyecto':proyecto})


@login_required
def detalle_proyecto(request,proyecto_id):
    proyecto=get_object_or_404(Proyecto,id=proyecto_id, usuario=request.user) 
    tareas=proyecto.tarea_set.all()
    
    if request.method=="POST":
        
        form=TareaForm(request.POST)
        
        if form.is_valid():
            tarea=form.save(commit=False)
            tarea.proyecto=proyecto
            tarea.save()
            
            return redirect('detalle_proyecto',proyecto_id=proyecto_id)
        
    else:
        form=TareaForm()
    return render(request,'detalle_proyecto.html',{
        'proyecto':proyecto,
        'tareas': tareas,
        'form': form
        })

@login_required
def toggle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    tarea.completada = not tarea.completada
    tarea.save()

    return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'editar_proyecto.html', {'form': form})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyectos')

    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})


@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'editar_tarea.html', {'form': form, 'tarea':tarea})


@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        proyecto_id = tarea.proyecto.id  # guardamos antes de eliminar
        tarea.delete()
        return redirect('detalle_proyecto', proyecto_id=proyecto_id)

    return render(request, 'eliminar_tarea.html', {
        'tarea': tarea
    })