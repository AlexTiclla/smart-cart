import os
import django
import pandas as pd

# Configurar entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcart.settings')
django.setup()

from ventas.models import Transaccion, Producto, DetalleTransaccion

# Cargar el CSV
df = pd.read_csv('transacciones.csv')

# Limpiar datos previos (opcional)
Transaccion.objects.all().delete()
Producto.objects.all().delete()
DetalleTransaccion.objects.all().delete()

# Insertar datos
for codigo in df['id_transaccion'].unique():
    transaccion, _ = Transaccion.objects.get_or_create(codigo=codigo)
    productos = df[df['id_transaccion'] == codigo]['producto']
    for nombre_producto in productos:
        producto, _ = Producto.objects.get_or_create(nombre=nombre_producto)
        DetalleTransaccion.objects.get_or_create(transaccion=transaccion, producto=producto)

print("✅ Datos insertados correctamente.")
