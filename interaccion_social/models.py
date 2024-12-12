from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from datetime import date, datetime, timedelta
from django.conf import settings

User = get_user_model()

##################  trabajos IIISP  ###################
    
    
class Estudiante(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Ru = models.CharField(max_length=20, null=True, blank=True)
    
class Docente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user.nombre}'

class Facultad(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.nombre


# Modelo de Carreras
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=150)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_carrera

# Modelo de Semestre
class Semestre(models.Model):
    S_Semestre=models.CharField(max_length=100,verbose_name='Semestre')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.S_Semestre
    
    
class Area(models.Model):
    nombre_area = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre_area

# Modelo de Materia
class Materia(models.Model):
    nombre_materia = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, unique=True)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre_materia

# Modelo de Gestión
class Gestion(models.Model):
    anio = models.IntegerField(unique=True)
    
    def __str__(self):
         return str(self.anio)

# Modelo de Periodos
class Periodo(models.Model):
    numero = models.IntegerField()
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-numero','-gestion__anio']  
    
    def __str__(self):
        return f'{self.numero}/{self.gestion.anio}'


class T_Tipo(models.Model):
    Id_tipo=models.AutoField(primary_key=True)
    S_Tipo= models.CharField(max_length=100, verbose_name='Tipo de Investigación Social.')
    
    class Meta:
        verbose_name_plural = "Tipo de Proyectos "
        verbose_name = "Tipo Proyecto"
    
    def __str__(self):
        return self.S_Tipo

class T_Fase(models.Model):
    Id_fase= models.AutoField(primary_key=True)
    S_Fase=models.CharField(max_length=100,verbose_name='Fase o Etapa del Proyecto')
    
    class Meta:
        verbose_name_plural = "Fases del Proyecto "
        verbose_name = "Fase Proyecto"
    
    def __str__(self):
        return self.S_Fase 
        
class T_Proyectos_IIISP(models.Model):
    Id_Proyect = models.AutoField(primary_key=True)
    S_persona = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario relacionado')
    S_Titulo = models.CharField(max_length=150, verbose_name='Título')
    Fecha_Inicio = models.DateField(auto_now=False, auto_now_add=False)
    Fecha_Finalizacion = models.DateField(auto_now=False, auto_now_add=False)
    S_Descripcion = models.TextField(verbose_name='Descripción', blank=True)
    S_Documentacion = models.FileField(upload_to='Documento/', verbose_name='Documentación', null=True)
    S_Imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    T_Fase_proyecto = models.ForeignKey(T_Fase, on_delete=models.CASCADE, verbose_name='Fase del Proyecto')
    T_Gestion = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name='Gestion')
    T_Tipo_Proyecto = models.ForeignKey(T_Tipo, on_delete=models.CASCADE, verbose_name='Tipo de Proyecto')
    T_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Materia')
     
    class Meta:
        verbose_name_plural = "Proyectos IIISP"
        verbose_name = "Trabajos IIISP"
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.Fecha_Finalizacion < self.Fecha_Inicio:
            raise ValidationError('La fecha de finalización debe ser posterior a la fecha de inicio.')
        
    def __str__(self):
        return self.S_Titulo
    
class HabilitarFechas(models.Model):
    fecha_inicio_habilitacion = models.DateField(null=True, blank=True, verbose_name='Fecha de Inicio de Habilitación')
    fecha_fin_habilitacion = models.DateField(null=True, blank=True, verbose_name='Fecha Fin de Habilitación')
    
    class Meta:
        verbose_name_plural = "Habilitacion de Fechas"
        verbose_name = "Habilitar Fecha"

    def __str__(self):
        return "Configuración Global"

    def tiempo_restante(self):
        hoy = datetime.now()
        if self.fecha_fin_habilitacion:
            fecha_fin = datetime.combine(self.fecha_fin_habilitacion, datetime.min.time())
            tiempo_restante = fecha_fin - hoy

            if tiempo_restante.days >= 0:
                dias = tiempo_restante.days
                horas = tiempo_restante.seconds // 3600
                return f"{dias} días y {horas} horas"
        
        return "0 Tiempo"
  

    
    
    
  

