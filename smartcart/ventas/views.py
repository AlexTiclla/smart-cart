import pandas as pd
from django.shortcuts import render
from ventas.models import Transaccion, DetalleTransaccion
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def reglas_apriori(request):
    # Cargar transacciones
    datos = []
    transacciones = Transaccion.objects.all()
    for trans in transacciones:
        productos = trans.detalletransaccion_set.all().values_list('producto__nombre', flat=True)
        datos.append(list(productos))

    # Uno-hot encoding
    te = TransactionEncoder()
    df_encoded = pd.DataFrame(te.fit_transform(datos), columns=te.columns_)

    # Apriori
    frecuentes = apriori(df_encoded, min_support=0.01, use_colnames=True)
    reglas = association_rules(frecuentes, metric="confidence", min_threshold=0.3)

    # Convertir a listas para enviar al template
    reglas['antecedents'] = reglas['antecedents'].apply(lambda x: ', '.join(list(x)))
    reglas['consequents'] = reglas['consequents'].apply(lambda x: ', '.join(list(x)))
    reglas_data = reglas[['antecedents', 'consequents', 'support', 'confidence', 'lift']].to_dict(orient='records')

    return render(request, 'ventas/reglas_apriori.html', {'reglas': reglas_data})
