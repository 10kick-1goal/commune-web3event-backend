from django.urls import path
# from django.conf.urls import url
from .views import  *

urlpatterns = [
    path('web3events/', get_all_events, name = 'get_all_events'),
    path('web3events/new/', create_event, name = 'create_event'),
    path('event_url/new/', create_event_url, name = 'create_event_url'),
    # url(r'^$', MainPage.as_view())
    
    # path('web3events/<int:pk>/', views.event_detail, name = 'event_detail'),
]