from apscheduler.schedulers.background import BackgroundScheduler
from eventscraping.geteventData import get_event_list
from eventscraping.geteventData import get_event_detail
from datetime import datetime

def start_scraper():
    print("start scraping!")
    # listScheduler = BackgroundScheduler()
    # listScheduler.add_job(get_event_list, 'interval', minutes = 1, start_date = datetime.now())
    # listScheduler.start()

    # detailScheduler = BackgroundScheduler()
    # detailScheduler.add_job(getlist.get_detail_info, 'interval', minutes = 2, start_date = datetime.now())
    # detailScheduler.start()
   
    # start_date=datetime.now()
    # get_list_result = get_event_list()
    get_list_result = True
    get_detail_result = get_event_detail(get_list_result)