import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcart.settings')
django.setup()

from ventas.models import Producto, Transaccion, DetalleTransaccion

# Verificar si existe "Espejo", si no lo crea
espejo, creado = Producto.objects.get_or_create(nombre="Espejo")
if creado:
    print("✅ Producto 'Espejo' creado.")
else:
    print("⚠️ El producto 'Espejo' ya existía.")

# Obtener transacciones aleatorias
transacciones = list(Transaccion.objects.all())
seleccionadas = random.sample(transacciones, min(10, len(transacciones)))

# Insertar "Espejo" en las transacciones seleccionadas
insertados = 0
for transaccion in seleccionadas:
    ya_existe = DetalleTransaccion.objects.filter(
        transaccion=transaccion, producto=espejo).exists()
    if not ya_existe:
        DetalleTransaccion.objects.create(
            transaccion=transaccion, producto=espejo)
        insertados += 1

print(f"🛒 Se insertó 'Espejo' en {insertados} transacciones.")
