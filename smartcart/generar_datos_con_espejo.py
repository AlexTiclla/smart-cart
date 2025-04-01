import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcart.settings')
django.setup()

from ventas.models import Producto, Transaccion, DetalleTransaccion

# Lista de productos
productos_base = [
    "Smartphone", "Auriculares", "Cargador", "Protector de Pantalla",
    "Laptop", "Mouse", "Teclado", "Tablet", "Power Bank", "Smartwatch"
]

# Crear productos base
producto_objs = {}
for nombre in productos_base:
    producto_objs[nombre], _ = Producto.objects.get_or_create(nombre=nombre)

# Agregar "Espejo"
producto_objs["Espejo"], _ = Producto.objects.get_or_create(nombre="Espejo")

# Crear 300 transacciones
num_transacciones = 300
transacciones = []
for i in range(num_transacciones):
    codigo = f"T{i+1:04d}"
    trans = Transaccion.objects.create(codigo=codigo)
    num_productos = random.randint(2, 5)
    productos = random.sample(productos_base, num_productos)
    for nombre in productos:
        DetalleTransaccion.objects.create(
            transaccion=trans,
            producto=producto_objs[nombre]
        )
    transacciones.append(trans)

# Insertar "Espejo" en solo 5 transacciones aleatorias
seleccionadas = random.sample(transacciones, 5)
for trans in seleccionadas:
    DetalleTransaccion.objects.create(
        transaccion=trans,
        producto=producto_objs["Espejo"]
    )

print("✅ Transacciones generadas y 'Espejo' insertado en 5 transacciones.")
