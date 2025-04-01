import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcart.settings')
django.setup()

from ventas.models import Producto, Transaccion, DetalleTransaccion

DetalleTransaccion.objects.all().delete()
Transaccion.objects.all().delete()
Producto.objects.all().delete()

print("🧹 Base de datos limpiada: se eliminaron todos los productos, transacciones y detalles.")
