from django.db import models

# Create your models here.
class Pagos(models.Model):

    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    img_url = models.CharField(max_length=200)
    detail = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tbl_pagos'

