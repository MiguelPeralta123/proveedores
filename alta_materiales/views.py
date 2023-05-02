from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import MaterialForm, MaterialFormForStaff, MaterialDetailForm
from .models import Material
# Decorator to protect routes from accessing before sign in
from django.contrib.auth.decorators import login_required

# Create your views here.

# VISTAS DE PROVEEDOR (GET ALL, CREATE, DETAIL)

@login_required
def material(request):
    # Trayendo de la base de datos los materiales que correspondan al usuario logueado
    materiales = Material.objects.filter(usuario = request.user)
    return render(request, 'material/material.html', {
        'materiales': materiales
    })

@login_required
def material_create(request):
    # Verificamos si el usuario tiene permisos para requerir, en caso contrario, lo redireccionamos a la ventana de materiales
    if request.user.puede_comprar:
        if request.method == 'GET':
            return render(request, 'material/material_create.html', {
                'form': MaterialForm
            })
        else:
            try:
                form = MaterialForm(request.POST)
                new_material = form.save(commit=False)
                new_material.usuario = request.user
                new_material.save()
                return redirect('material')
            except ValueError:
                return render(request, 'material/material_create.html', {
                    'form': MaterialForm,
                    'error': 'Por favor ingrese datos válidos'
                })
    else:
        return redirect('material')

@login_required
def material_detail(request, material_id):
    # Traemos el proveedor que tenga el id que seleccionamos
    material = get_object_or_404(Material, pk=material_id, usuario=request.user)
    if request.method == 'GET':
        # Creamos un formulario con los datos del material precargados
        # Validamos si el usuario es staff para mostrar la información completa
        if request.user.is_staff:
            form = MaterialFormForStaff(instance=material)
        else:
            form = MaterialDetailForm(instance=material)
        return render(request, 'material/material_detail.html', {
            'material': material,
            'form': form
        })
    else:
        try:
            form = MaterialDetailForm(request.POST, instance=material)
            form.save()
            return redirect('material')
        except ValueError:
            form = MaterialDetailForm(instance=material)
            return render(request, 'material/material_detail.html', {
                'material': material,
                'form': form,
                'error': 'Se produjo un error al actualizar, intente de nuevo'
            })