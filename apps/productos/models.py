from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    estado = models.BooleanField()
    detail = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tbl_categoria'


class Productos(models.Model):

    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.CharField(max_length=200)
    stock = models.IntegerField()
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    detail = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tbl_productos'
