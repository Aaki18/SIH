from django.apps import AppConfig

class AlumniAppConfig(AppConfig):
    name = 'alumni_app'
    verbose_name = 'Alumni Application'

    def ready(self):
        # This is where you can put any startup code, signals, or other app initialization.
        pass
