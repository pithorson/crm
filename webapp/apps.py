from django.apps import AppConfig


class WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp'


class MyAppConfig(AppConfig):
    name = 'webapp'

    def ready(self):
        import webapp.templatetags.custom_tags