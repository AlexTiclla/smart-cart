import os
import django
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartcart.settings')
django.setup()

from ventas.models import Transaccion, DetalleTransaccion

# Paso 1: Cargar las transacciones desde la BD
datos = []

transacciones = Transaccion.objects.all()

for trans in transacciones:
    productos = trans.detalletransaccion_set.all().values_list('producto__nombre', flat=True)
    datos.append(list(productos))

# Paso 2: Convertir a formato de "basket" (uno-hot encoding por fila)
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(datos).transform(datos)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Paso 3: Aplicar Apriori
frecuentes = apriori(df, min_support=0.01, use_colnames=True)

# Paso 4: Generar reglas de asociación
reglas = association_rules(frecuentes, metric="confidence", min_threshold=0.3)

# Paso 5: Mostrar resultados
if not reglas.empty:
    pd.set_option('display.max_rows', None)       # muestra todas las filas
    pd.set_option('display.max_columns', None)    # muestra todas las columnas
    pd.set_option('display.max_colwidth', None)   # muestra todo el contenido de celdas

    print("📊 Reglas encontradas:\n")
    print(reglas[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
else:
    print("⚠️ No se encontraron reglas frecuentes con los parámetros dados.")
