from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class LogConfig(AppConfig):
    name = 'log'
    verbose_name = _('Log')
    
    def ready(self):
        import home.signals