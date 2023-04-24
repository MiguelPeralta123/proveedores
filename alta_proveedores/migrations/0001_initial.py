# Generated by Django 4.2 on 2023-04-22 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('tipo_alta', models.CharField(max_length=20)),
                ('proveedor', models.CharField(max_length=10)),
                ('contribuyente', models.CharField(max_length=20)),
                ('razon_social', models.CharField(max_length=50)),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(blank=True, max_length=18)),
                ('regimen_capital', models.CharField(max_length=100)),
                ('nombre_comercial', models.CharField(max_length=50)),
                ('regimen_fiscal', models.CharField(max_length=100)),
                ('uso_cdfi', models.CharField(max_length=100)),
                ('representante_legal', models.CharField(blank=True, max_length=50)),
                ('correo_contacto', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=10)),
                ('correo_pagos', models.CharField(max_length=30)),
                ('sitio_web', models.CharField(blank=True, max_length=30)),
                ('rubro', models.CharField(max_length=20)),
                ('tipo_operacion', models.CharField(max_length=10)),
                ('dias_credito', models.IntegerField(default=0)),
                ('monto_credito', models.IntegerField(default=0)),
                ('retencion_iva', models.CharField(max_length=10)),
                ('retencion_isr', models.CharField(max_length=10)),
                ('iva_frontera', models.CharField(max_length=10)),
                ('calle', models.CharField(max_length=50)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(blank=True, max_length=10)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('colonia', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50)),
                ('cuenta', models.CharField(max_length=10)),
                ('moneda', models.CharField(max_length=3)),
                ('clabe', models.CharField(max_length=18)),
                ('banco2', models.CharField(blank=True, max_length=50)),
                ('cuenta2', models.CharField(blank=True, max_length=10)),
                ('moneda2', models.CharField(blank=True, max_length=3)),
                ('clabe2', models.CharField(blank=True, max_length=18)),
                ('constancia_situacion_fiscal', models.FileField(upload_to='')),
                ('estado_cuenta_bancario', models.FileField(upload_to='')),
                ('compras', models.BooleanField(default=False)),
                ('finanzas', models.BooleanField(default=False)),
                ('sistemas', models.BooleanField(default=False)),
                ('aprobadas', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]