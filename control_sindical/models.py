from django.db import models
from datetime import date

# Create your models here.
class Sindicato(models.Model):
    dirección = models.CharField(max_length=100, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
class Trabajador(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    ci = models.IntegerField(max_length=11, blank=False, null=False)
    salario_mensual = models.FloatField(blank=False, null=False)
    cuota = models.FloatField(blank=False, null=False)
    fecha_alta = models.DateField(default=date.today, blank=False, null=False)
    fecha_baja = models.DateField(blank=True, null=True)
    sindicato = models.ForeignKey(Sindicato, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Map(models.Model):
    monto = models.FloatField(blank=False, null=False)
    fecha_pago = models.DateField(blank=False, null=False)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Trabajador: {}, Fecha de pago: {}, Monto: {}"
        return txt.format(self.trabajador, self.fecha_pago, self.monto)
    
class AsambleaAfiliados(models.Model):
    fecha = models.DateField(default=date.today, blank=False, null=False)
    cantidad_trabajadores = models.IntegerField(blank=False, null=False)
    cantidad_acuerdos = models.IntegerField(blank=False, null=False)
    sindicato = models.ForeignKey(Sindicato, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Sindicato: {}, Cantidad de acuerdos: {}, Fecha: {}"
        return txt.format(self.sindicato, self.cantidad_acuerdos, self.fecha)
