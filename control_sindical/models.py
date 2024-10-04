from django.db import models
from datetime import date
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.
class Sindicato(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    dirección = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre
    
class Trabajador(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    ci = models.IntegerField(blank=False, null=False)
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
    pagado = models.BooleanField(default=False)

    def __str__(self):
        txt = "Trabajador: {}, Fecha de pago: {}, Monto: {}"
        return txt.format(self.trabajador, self.fecha_pago, self.monto)
    
class AsambleaAfiliados(models.Model):
    fecha = models.DateField(default=date.today, blank=False, null=False)
    cantidad_trabajadores = models.IntegerField(blank=False, null=False)
    cantidad_acuerdos = models.IntegerField(blank=False, null=False)
    sindicato = models.ForeignKey(Sindicato, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_asamblea/', null=True, blank=True, default='path/media/default_image.jpg')

    def __str__(self):
        txt = "Sindicato: {}, Cantidad de acuerdos: {}, Fecha: {}"
        return txt.format(self.sindicato, self.cantidad_acuerdos, self.fecha)



#----------------------------------------------------------------------------

@receiver(pre_delete, sender=AsambleaAfiliados)
def eliminar_imagen_de_asamblea(sender, instance, **kwargs):
    # Verificar si el área tiene una imagen asociada y eliminarla
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

@receiver(pre_save, sender=AsambleaAfiliados)
def eliminar_imagen_anterior_al_actualizar(sender, instance, **kwargs):
    if not instance.pk:  # El área es nueva, no hay imagen anterior que eliminar
        return False

    try:
        area_anterior = Area.objects.get(pk=instance.pk)  # Obtener el área anterior de la base de datos
    except Area.DoesNotExist:
        return False  # El área anterior no existe, no hay imagen anterior que eliminar

    if area_anterior.imagen:  # Verificar si el área anterior tiene una imagen
        nueva_imagen = instance.imagen
        if area_anterior.imagen != nueva_imagen:  # Verificar si se ha seleccionado una nueva imagen
            if os.path.isfile(area_anterior.imagen.path):  # Verificar si el archivo de imagen existe en el sistema de archivos
                os.remove(area_anterior.imagen.path)                