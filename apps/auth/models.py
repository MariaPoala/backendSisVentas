from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group


class UserProfileManager(BaseUserManager):
    """Manager para perfil de usuarios"""

    def create_user(self, name, persona, password=None, ):
        user = self.model(name=name)
        user.persona_id = persona
        user.name = name
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name, usuario, persona, password):
        user = self.create_user(name, password)
        user.usuario = usuario
        user.persona_id = persona
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema"""

    name = models.CharField(max_length=255)
    usuario = models.CharField(max_length=20, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    objects = UserProfileManager()
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

class Persona(models.Model):
    # * SOL 1.00 - DOL 3.98
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=20, null=True)
    dni = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    direccion = models.CharField(max_length=255, null=True)
    data = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        db_table = 'persona'