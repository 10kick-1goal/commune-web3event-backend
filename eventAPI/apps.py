from django.apps import AppConfig
from django.db.models.signals import post_migrate
import sys
sys.path.insert(0, '../eventscraping')
class eventAPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eventAPI'

    print('---11===------------')

    def ready(self):
    #     post_migrate.connect( self.on_post_migrate, sender = self )

    # def on_post_migrate( self, sender, **kwargs ):
        from eventscraping.scraper import start_scraper
        start_scraper()
        if not getattr(self, '_already_called', False):
            self._already_called = True
        
