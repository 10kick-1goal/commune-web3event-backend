from eventscraping.scraping_control.get_event_url import get_list_luma
from eventscraping.scraping_control.get_event_url import get_list_eventbrite
from eventscraping.scraping_control.get_detail_info import get_detail_info_luma
from eventscraping.scraping_control.get_detail_info import get_detail_info_eventbrite

from db_control.event_url_control import create_event_url
from db_control.event_url_control import getAll_event_url
# from db_control.event_url_control import getsome_event_url
from db_control.web3event_control import create_event

import json
from datetime import datetime

def get_event_list():
    print("start getting event-urls!")
    try:
        event_list_luma = get_list_luma()
        print("eventurlLuma:", len(event_list_luma))
        for event_url in event_list_luma:
            create_event_url(event_url, "1")

        event_list_eventbrite = get_list_eventbrite()
        print("eventurlEventbrite:", len(event_list_eventbrite))
        for event_url in event_list_eventbrite:
            create_event_url(event_url, "2")

        print("get event-url successfully")
        return True
    except:
        print("get event-url failed")
        return False
    


def get_event_detail(flag):
    if flag:
        print("start getting events details!")
        try:
            event_urls = getAll_event_url()  
            print("event_urls", event_urls)
                
            event_urls_test = event_urls[:5]
            event_detail_list = [ get_detail_info(event_url) for event_url in event_urls_test if get_detail_info(event_url) is not None ]
            
            print("get event detail info successfully")
            for event_detail in event_detail_list:
                # if event_detail["title"] == "":
                #     continue

                create_event(event_detail)
            return True
        except:
            print("get event detail info failed")
            return False
    else:
        print("there are not updated event urls")
        return False

#     return get_event_list()

def get_detail_info(event_url):
    site_type = event_url.site_type
    if site_type == "1":
        event_detail_info = get_detail_info_luma(event_url)
    elif site_type == "2":
        event_detail_info = get_detail_info_eventbrite(event_url)
    else:
        event_detail_info = None
    return event_detail_info