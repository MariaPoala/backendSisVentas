from django.db import models
# from django.utils.timezone import now

# from apps.auth.models import AuthUser
# from apps.productos.models import Productos
# from apps.utils.models import Cliente

# class Ventas(models.Model):
#     ESTADOS_VENTA = [
#         ('activa', 'Activa'),
#         ('anulada', 'Anulada'),
#     ]

#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     usuario = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="ventas_realizadas")
#     tipo_comprobante = models.CharField(max_length=200)
#     fecha = models.DateTimeField()
#     estado = models.CharField(max_length=10, choices=ESTADOS_VENTA, default='activa')
    
#     # Información de anulación
#     anulado_por = models.ForeignKey(AuthUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="ventas_anuladas")
#     fecha_anulacion = models.DateTimeField(null=True, blank=True)

#     # Timestamps
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)

#     class Meta:
#         db_table = 'tbl_ventas'

#     def anular(self, usuario):
#         """Método para anular una venta"""
#         self.estado = 'anulada'
#         self.anulado_por = usuario
#         self.fecha_anulacion = now()
#         self.save()


# class DetalleVenta(models.Model):
#     ventas = models.ForeignKey('Ventas', on_delete=models.CASCADE)
#     producto= models.ForeignKey(Productos, on_delete=models.CASCADE)
#     cantidad= models.DecimalField(max_digits=10, decimal_places=2)
#     precio_unitario= models.DecimalField(max_digits=10, decimal_places=2)
#     detail = models.JSONField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)

#     class Meta:
#         db_table = 'tbl_detalleventa'


# class Pagos(models.Model):
#     ventas = models.ForeignKey('Ventas', on_delete=models.CASCADE)
#     metodo_pago= models.ForeignKey(Productos, on_delete=models.CASCADE)
#     monto= models.DecimalField(max_digits=10, decimal_places=2)
#     fecha = models.DateTimeField()
#     detail = models.JSONField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)

#     class Meta:
#         db_table = 'tbl_pagos'

        