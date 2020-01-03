from vizsla import settings

class AppRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label in settings.APP_SCHEMAS :
            return model._meta.app_label
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in settings.APP_SCHEMAS :
            return model._meta.app_label
        return None

