from django.apps import AppConfig


class EgliseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eglise'

    def ready(self):
        # Importer les signaux quand l'application est chargée
        try:
            import eglise.signals  # noqa: F401
        except Exception:
            # Vous pouvez activer un log ici si vous voulez suivre les erreurs
            pass
