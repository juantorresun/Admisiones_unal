from django.db import models

# Create your models here.
class Periodo(models.Model):
    idperiodo = models.IntegerField()
    año = models.CharField(max_length=45)
    semestre = models.CharField(max_length=45)
    Tipo = models.CharField(max_length=45)
    Estado = models.CharField(max_length=45)
    Fecha_inicio = models.CharField(max_length=45)
    Fecha_cierre = models.CharField(max_length=45)



class Cupo (models.Model):
    sede = models.CharField(max_length=45)
    programa = models.CharField(max_length=100)
    tipo_programa = models.CharField(max_length=45)
    numero_cupos = models.CharField(max_length=45)
    semestre= models.CharField(max_length=45)
    año= models.CharField(max_length=45)


class Inscripcion (models.Model):
    periodo = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    tipo_documento = models.CharField(max_length=45)
    documento = models.CharField(max_length=45)
    nombre = models.CharField(max_length=200)
    tipo_ins= models.CharField(max_length=45)
    programa= models.CharField(max_length=45)
    pin= models.CharField(max_length=45)