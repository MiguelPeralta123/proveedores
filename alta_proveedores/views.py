from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import ProveedorForm, ProveedorDetailForm, ProveedorFormForCompras, ProveedorFormForFinanzas, ProveedorFormForSistemas
from .models import Proveedor
# Decorator to protect routes from accessing before sign in
from django.contrib.auth.decorators import login_required

# Create your views here.

# VISTA DE INICIO

# Using the decorator to force login, the return route to login is defined in proveedores/settings.py
@login_required
def home(request):
    return render(request, 'home.html')

# VISTAS DE INICIO DE SESIÓN (SIGNUP, LOGIN, LOGOUT)

def signup(request):
    # Si accedemos a la página de signup con GET, devolvemos el formulario
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    # Si accedemos con POST, enviamos los valores de los input a '/signup'
    else:
        # Si las contraseñas coinciden, guardamos el usuario
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'})
        # Si no, devolvemos un mensaje
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'})

def signin(request):
    # Si accedemos a la página de login con GET, devolvemos el formulario
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    # Si accedemos con POST, enviamos los valores de los input a '/signin'
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario y/o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')

def signout(request):
    logout(request)
    return redirect('signin')

# VISTAS DE PROVEEDOR (GET ALL, CREATE, DETAIL)

@login_required
def proveedor(request):
    # Si el usuario tiene permisos de compras, podrá ver las solicitudes de todos los usuarios
    if request.user.compras:
        # Trayendo de la base de datos todas las solicitudes que no hayan sido aprobadas por compras
        proveedores = Proveedor.objects.filter(compras = False)
    else:
        if request.user.finanzas:
            # Trayendo de la base de datos todas las solicitudes que no hayan sido aprobadas por finanzas
            proveedores = Proveedor.objects.filter(compras = True, finanzas = False)
        else:
            if request.user.sistemas:
                # Trayendo de la base de datos todas las solicitudes que no hayan sido aprobadas por sistemas
                proveedores = Proveedor.objects.filter(compras = True, finanzas = True, sistemas = False)
            else:
                # Trayendo de la base de datos los proveedores que correspondan al usuario logueado
                proveedores = Proveedor.objects.filter(usuario = request.user)
    return render(request, 'proveedor/proveedor.html', {
            'proveedores': proveedores
        })

@login_required
def proveedor_create(request):
    # Verificamos si el usuario tiene permisos para requerir, en caso contrario, lo redireccionamos a la ventana de proveedores
    if request.user.puede_comprar:
        if request.method == 'GET':
            return render(request, 'proveedor/proveedor_create.html', {
                'form': ProveedorForm
            })
        else:
            try:
                form = ProveedorForm(request.POST, request.FILES)
                new_proveedor = form.save(commit=False)
                new_proveedor.usuario = request.user
                new_proveedor.save()
                return redirect('proveedor')
            except ValueError:
                return render(request, 'proveedor/proveedor_create.html', {
                    'form': ProveedorForm,
                    'error': 'Por favor ingrese datos válidos'
                })
    else:
        return redirect('proveedor')

@login_required
def proveedor_detail(request, proveedor_id):
    # Traemos el proveedor que tenga el id que seleccionamos
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'GET':
        # Validamos si el usuario es compras para mostrar el checkbox para aprobar
        if request.user.compras:
            form = ProveedorFormForCompras(instance=proveedor)
        else:
            if request.user.finanzas:
                form = ProveedorFormForFinanzas(instance=proveedor)
            else:
                if request.user.sistemas:
                    form = ProveedorFormForSistemas(instance=proveedor)
                else:
                    form = ProveedorDetailForm(instance=proveedor)
        return render(request, 'proveedor/proveedor_detail.html', {
            'proveedor': proveedor,
            'form': form
        })
    else:
        try:
            if request.user.compras:
                form = ProveedorFormForCompras(request.POST, instance=proveedor)
            else:
                if request.user.finanzas:
                    form = ProveedorFormForFinanzas(request.POST, instance=proveedor)
                else:
                    if request.user.sistemas:
                        form = ProveedorFormForSistemas(request.POST, instance=proveedor)
                    else:
                        form = ProveedorDetailForm(request.POST, instance=proveedor)
            form.save()
            return redirect('proveedor')
        except ValueError:
            form = ProveedorDetailForm(instance=proveedor)
            return render(request, 'proveedor/proveedor_detail.html', {
                'proveedor': proveedor,
                'form': form,
                'error': 'Se produjo un error al actualizar, intente de nuevo'
            })