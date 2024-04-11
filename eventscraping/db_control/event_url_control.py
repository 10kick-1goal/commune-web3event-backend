from eventAPI.models import EventUrl

def create_event_url(event_href, site_type):
    event_url = event_href.get('href')
    site_type  = site_type
    EventUrl.objects.create(source_url = event_url, site_type = site_type)

def getAll_event_url():
    eventUrls = EventUrl.objects.all()
    return eventUrls

