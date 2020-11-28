from django.apps import AppConfig


class PayementsConfig(AppConfig):
    name = 'payements'

    def ready(self):
        import payements.signals
