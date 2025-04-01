from django.urls import path
from . import views

urlpatterns = [
    path('reglas/', views.reglas_apriori, name='reglas_apriori'),
]
