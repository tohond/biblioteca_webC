from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

def validar_nombre(value):
    # Valida que el nombre no esté vacío ni contenga solo espacios
    if not value or not value.strip():
        raise ValidationError("El nombre no puede estar vacío o solo espacios.")

def validar_longitud_resumen(value):
    # Por ejemplo, aseguramos que el resumen tenga al menos 20 caracteres
    if len(value.strip()) < 20:
        raise ValidationError("El resumen debe tener al menos 20 caracteres.")

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_longitud_resumen])

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    # Validamos que la calificación esté entre 1 y 5
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
