from django.apps import AppConfig
from django.core.signals import setting_changed


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'


    def ready(self):
        # cuando la app esté lista conectamos la señal
        from .signals import actualizarProducto

        setting_changed.connect(actualizarProducto)
