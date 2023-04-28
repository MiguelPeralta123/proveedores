from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'calle', 'numero_exterior', 'numero_interior', 'codigo_postal', 'colonia', 'localidad', 'municipio', 'ciudad', 'estado', 'pais', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'constancia_situacion_fiscal', 'estado_cuenta_bancario']
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.TextInput(attrs={'class':'form-control'}),
            'contribuyente': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'uso_cdfi': forms.TextInput(attrs={'class':'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_operacion': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_tercero': forms.TextInput(attrs={'class':'form-control'}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_isr': forms.TextInput(attrs={'class':'form-control'}),
            'iva_frontera': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.TextInput(attrs={'class':'form-control'}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.TextInput(attrs={'class':'form-control'}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'constancia_situacion_fiscal': forms.FileInput(attrs={'class':'form-file'}),
            'estado_cuenta_bancario': forms.FileInput(attrs={'class':'form-file'}),
        }

class ProveedorDetailForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'calle', 'numero_exterior', 'numero_interior', 'codigo_postal', 'colonia', 'localidad', 'municipio', 'ciudad', 'estado', 'pais', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'constancia_situacion_fiscal', 'estado_cuenta_bancario']
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.TextInput(attrs={'class':'form-control'}),
            'contribuyente': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'uso_cdfi': forms.TextInput(attrs={'class':'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_operacion': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_tercero': forms.TextInput(attrs={'class':'form-control'}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.TextInput(attrs={'class':'form-control'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_isr': forms.TextInput(attrs={'class':'form-control'}),
            'iva_frontera': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.TextInput(attrs={'class':'form-control'}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.TextInput(attrs={'class':'form-control'}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'constancia_situacion_fiscal': forms.FileInput(attrs={'class':'form-file'}),
            'estado_cuenta_bancario': forms.FileInput(attrs={'class':'form-file'}),
        }

class ProveedorFormForStaff(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'calle', 'numero_exterior', 'numero_interior', 'codigo_postal', 'colonia', 'municipio', 'ciudad', 'estado', 'pais', 'banco', 'cuenta', 'moneda', 'clabe', 'compras', 'finanzas', 'sistemas']
        
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.TextInput(attrs={'class':'form-control'}),
            'contribuyente': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'uso_cdfi': forms.TextInput(attrs={'class':'form-control'}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_operacion': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_isr': forms.TextInput(attrs={'class':'form-control'}),
            'iva_frontera': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.TextInput(attrs={'class':'form-control'}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.TextInput(attrs={'class':'form-control'}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'compras': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'finanzas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'sistemas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }