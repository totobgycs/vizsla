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

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in settings.APP_SCHEMAS:
            return True
        return None

