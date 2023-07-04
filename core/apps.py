from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    # Override the ready() method to import our signals.py file
    def ready(self):
        import core.signals
