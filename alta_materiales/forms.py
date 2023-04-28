from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['empresa', 'nombre_producto', 'tipo', 'familia', 'subfamilia', 'unidad_medida', 'justificacion']
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'familia': forms.TextInput(attrs={'class':'form-control'}),
            'subfamilia': forms.TextInput(attrs={'class':'form-control'}),
            'unidad_medida': forms.TextInput(attrs={'class':'form-control'}),
            'justificacion': forms.Textarea(attrs={'class':'form-control'}),
        }


class MaterialDetailForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['empresa', 'nombre_producto', 'tipo', 'familia', 'subfamilia', 'unidad_medida', 'justificacion', 'compras', 'finanzas', 'sistemas']
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'familia': forms.TextInput(attrs={'class':'form-control'}),
            'subfamilia': forms.TextInput(attrs={'class':'form-control'}),
            'unidad_medida': forms.TextInput(attrs={'class':'form-control'}),
            'justificacion': forms.Textarea(attrs={'class':'form-control'}),
            'compras': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'finanzas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'sistemas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }

class MaterialFormForStaff(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['empresa', 'nombre_producto', 'tipo', 'familia', 'subfamilia', 'unidad_medida', 'justificacion', 'compras', 'finanzas', 'sistemas', 'usuario']
        widgets = {
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'familia': forms.TextInput(attrs={'class':'form-control'}),
            'subfamilia': forms.TextInput(attrs={'class':'form-control'}),
            'unidad_medida': forms.TextInput(attrs={'class':'form-control'}),
            'justificacion': forms.Textarea(attrs={'class':'form-control'}),
            'compras': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'finanzas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'sistemas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'usuario': forms.CharField(),
        }