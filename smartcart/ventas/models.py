from django.db import models

class Transaccion(models.Model):
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.codigo

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class DetalleTransaccion(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transaccion} - {self.producto}"
