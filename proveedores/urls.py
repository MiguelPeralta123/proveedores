"""
URL configuration for proveedores project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Creamos los endpoints para las vistas de proveedores
from alta_proveedores import views
# Creamos los endpoints para las vistas de materiales
from alta_materiales import views as views_materiales

urlpatterns = [
    # URL para admin
    path('admin/', admin.site.urls),
    # URL para home
    path('', views.home, name='home'),
    # URLs para inicio de sesión (signup, login, logout)
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    # URLs para proveedores (get all, create, detail)
    path('proveedores/', views.proveedor, name='proveedor'),
    path('proveedores/crear/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/<int:proveedor_id>/', views.proveedor_detail, name='proveedor_detail'),
    # URLs para solicitudes y materiales
    path('materiales/', views_materiales.material, name='material'),
    path('materiales/crear/', views_materiales.material_create, name='material'),
    path('materiales/<int:material_id>/', views_materiales.material_detail, name='material_detail'),
]