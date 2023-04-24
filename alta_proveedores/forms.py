from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'tipo_alta', 'proveedor', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'correo_contacto', 'celular', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'calle', 'numero_exterior', 'numero_interior', 'codigo_postal', 'colonia', 'municipio', 'ciudad', 'estado', 'pais', 'banco', 'cuenta', 'moneda', 'clabe', 'banco2', 'cuenta2', 'moneda2', 'clabe2', 'constancia_situacion_fiscal', 'estado_cuenta_bancario']