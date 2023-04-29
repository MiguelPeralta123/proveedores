# Generated by Django 4.2 on 2023-04-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('tipo_alta', models.CharField(max_length=20)),
                ('contribuyente', models.CharField(max_length=20)),
                ('razon_social', models.CharField(max_length=50)),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(blank=True, max_length=18)),
                ('regimen_capital', models.CharField(max_length=100)),
                ('nombre_fiscal', models.CharField(max_length=100)),
                ('nombre_comercial', models.CharField(max_length=50)),
                ('uso_cdfi', models.CharField(max_length=100)),
                ('representante_legal', models.CharField(blank=True, max_length=50)),
                ('telefono_1', models.CharField(max_length=10)),
                ('telefono_2', models.CharField(max_length=10)),
                ('contacto', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
                ('correo_general', models.CharField(max_length=40)),
                ('correo_pagos', models.CharField(max_length=40)),
                ('sitio_web', models.CharField(blank=True, max_length=30)),
                ('rubro', models.CharField(max_length=20)),
                ('tipo_operacion', models.CharField(max_length=10)),
                ('tipo_tercero', models.CharField(max_length=20)),
                ('id_fiscal', models.CharField(max_length=10)),
                ('regimen_fiscal', models.CharField(max_length=100)),
                ('agente_aduanal', models.CharField(max_length=10)),
                ('reg_inc_fiscal', models.CharField(max_length=10)),
                ('impuesto_cedular', models.CharField(max_length=10)),
                ('venc_s_fecha', models.DateField()),
                ('dias_para_entrega_completa', models.PositiveIntegerField(default=0)),
                ('dias_credito', models.PositiveIntegerField(default=0)),
                ('limite_credito_MN', models.PositiveIntegerField(default=0)),
                ('limite_credito_ME', models.PositiveIntegerField(default=0)),
                ('monto_credito', models.PositiveIntegerField(default=0)),
                ('retencion_iva', models.CharField(max_length=10)),
                ('retencion_isr', models.CharField(max_length=10)),
                ('iva_frontera', models.CharField(max_length=10)),
                ('calle', models.CharField(max_length=50)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(blank=True, max_length=10)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('colonia', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50)),
                ('cuenta', models.CharField(max_length=10)),
                ('moneda', models.CharField(max_length=3)),
                ('clabe', models.CharField(max_length=18)),
                ('banco_2', models.CharField(blank=True, max_length=50)),
                ('cuenta_2', models.CharField(blank=True, max_length=10)),
                ('moneda_2', models.CharField(blank=True, max_length=3)),
                ('clabe_2', models.CharField(blank=True, max_length=18)),
                ('constancia_situacion_fiscal', models.FileField(upload_to='documentos/constancias/')),
                ('estado_cuenta_bancario', models.FileField(upload_to='documentos/estados_cuenta')),
                ('compras', models.BooleanField(default=False)),
                ('finanzas', models.BooleanField(default=False)),
                ('sistemas', models.BooleanField(default=False)),
                ('aprobadas', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usar_en_portal_proveedores', models.BooleanField(default=False)),
                ('no_aplica_para_rafaga', models.BooleanField(default=False)),
                ('no_relacionar_OC', models.BooleanField(default=False)),
            ],
        ),
    ]
