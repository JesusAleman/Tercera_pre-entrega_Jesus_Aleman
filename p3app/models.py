from django.db import models

# Create your models here.

class CatalogoVenta(models.Model):
    articulo= models.CharField(max_length=50)
    cantidad= models.IntegerField(null=False, blank=False)
    categoria= models.CharField(max_length=50)

    def __str__(self):
            return f"{self.articulo} cantidad: {self.cantidad} categoria: {self.categoria}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(null=False, blank=False)
    email = models.EmailField()
    rfc=models.CharField(max_length=13)

    def __str__(self):
            return f"nombre: {self.nombre},    Teléfono: {self.telefono}, Email: {self.email}, RFC:{self.rfc}"

class Socio(models.Model):
    empresa = models.CharField(max_length=50)
    paisdeorigen = models.CharField(max_length=50)

    def __str__(self):
            return f"empresa: {self.empresa},    País de Origen: {self.paisdeorigen}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    fechadenacimiento = models.DateField()
    email = models.EmailField()

    def __str__(self):
            return f"{self.nombre},    Fecha de Nacimiento: {self.fechadenacimiento},    email: {self.email}"

