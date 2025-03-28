from django.db import models

# Create your models here.

from apps.auth.models import AuthUser
# from apps.tecnic.models import StatesAverias
# from apps.utils.models import Clients


# Create your models here.
class Activities(models.Model):

    # cliente = models.ForeignKey(Clients, on_delete=models.CASCADE)
    descripcion = models.JSONField()
    usuario = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    direction = models.CharField(max_length=100)
    date_activity = models.CharField(max_length=20) #FORMATO TIMESTAMP UNIX
    prioridad = models.CharField(max_length=20)
    # state_activity = models.ForeignKey(StatesAverias, on_delete=models.CASCADE)
    class Meta:
        db_table = 'activities'
