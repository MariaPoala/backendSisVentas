from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre = models.CharField(max_length=150)
    nro_documento = models.CharField(max_length=500)
    telefono=models.CharField(max_length=500)
    direccion=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    detail = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tbl_cliente'

