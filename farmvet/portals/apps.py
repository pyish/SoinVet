from django.apps import AppConfig


class PortalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portals'

    def ready(self):
        import portals.signals 