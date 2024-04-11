import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.start_webdriver_2 import start_driver_2
from common.utils import remove_repeated_events
from common.utils import check_keywords_in_title
from common.categoies_list import web3_categories_list
from common.cities import web3event_cities
from common.tags import web3event_tags

def get_list_luma():
    driver = start_driver_2()
    luma_url = 'https://lu.ma'
    driver.get(luma_url+'/explore')
    WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "div.can-divide")) )
    list_luma = []
    event_sections = driver.find_elements(By.CSS_SELECTOR, 'div.can-divide')
    city_event_elements = event_sections[0].find_elements(By.TAG_NAME, 'a')
    calender_event_elements = event_sections[1].find_elements(By.TAG_NAME, 'a')

    city_event_href_values = [element.get_attribute('href') for element in city_event_elements]
    for city_href in city_event_href_values:
        list_luma.extend(get_event_url_luma(city_href, 'city'))


    calender_event_href_values = [element.get_attribute('href') for element in calender_event_elements]
    for calender_href in calender_event_href_values[0:5]:
        list_luma.extend(get_event_url_luma(calender_href, 'topic'))

    filtered_event_list = remove_repeated_events(list_luma, "href")
    return filtered_event_list

def get_event_url_luma(href, type):
    url = href
    driver = start_driver_2()
    driver.get(url)
    delay = 3
    time.sleep(delay)
    print("Page Loaded Completely")

    data_list = []
    try:
        if type == "topic":
            topic = driver.find_element(By.CSS_SELECTOR, 'div.jsx-212035885.flex-column.header h1')
            print(topic.text)
            print(web3_categories_list)
            is_topic = check_keywords_in_title(topic, web3_categories_list)
            if is_topic:
                is_web3 = True
            else:
                is_web3 = False

        else:
            is_web3 = False
        card_wrappers = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card-wrapper')))
        for card_wrapper in card_wrappers:
            unit_data = {}

            try:
                a_tag = card_wrapper.find_element(By.CSS_SELECTOR, 'a.event-link')
                unit_data['href'] = a_tag.get_attribute('href')

                h3_tag = card_wrapper.find_element(By.CLASS_NAME, 'jsx-3851280986')
                unit_data['title'] = h3_tag.text
                
                pill_labels = card_wrapper.find_elements(By.CLASS_NAME, 'jsx-146954525.pill-label')
                pill_label_texts = [label.text for label in pill_labels]
                unit_data['tags'] = pill_label_texts

                if is_web3:
                    data_list.append(unit_data)
                else:
                    isInclude = check_keywords_in_title(unit_data['title'], web3_categories_list)
                    if(isInclude):
                        data_list.append(unit_data)

            except NoSuchElementException:
                print("Unable to locate elements in card-wrapper")

    except TimeoutException:
        print("Timed out waiting for time line to load")
    except Exception as e:
        print(f'error: {e}')

    return data_list

def get_list_eventbrite():
    eventbrite_url = "https://www.eventbrite.com"
    list_eventbrite = []
    for city in web3event_cities:
        for tag in web3event_tags:
            url = eventbrite_url + "/d/" + city + "/" +tag
            list_eventbrite.extend(get_event_url_eventbrite(url))
    
    filtered_event_list = remove_repeated_events(list_eventbrite, "href")

    print("count:", len(filtered_event_list))

def get_event_url_eventbrite(url):
    url = url + "/?oage="
    driver = start_driver_2()
    try:
        event_list = []
        is_end = False
        page = 1
        while not is_end:
            page_url = url +str (page)
            driver.get(page_url)
            delay = 10
            time.sleep(delay)
            dom = bs(driver.page_source, "html.parser")
            try:
                search_result_element = driver.find_element(By.CSS_SELECTOR, "ul.SearchResultPanelContentEventCardList-module__eventList___1YEh_")
                is_search_result = search_result_element.is_displayed()
                page += 1
                event_elements = search_result_element.find_elements(By.TAG_NAME, "li")
                for element in event_elements:
                    event = {}
                    event_card = element.find_element(By.CSS_SELECTOR, "div.discover-search-desktop-card")
                    event_detail = event_card.find_element(By.CSS_SELECTOR, "section.event-card-details")
                    title_element = event_detail.find_element(By.CSS_SELECTOR, "div.Stack_root__1ksk7>a")
                    event_url = title_element.get_attribute("href")
                    event_title = title_element.text
                    event["href"] = event_url
                    event["title"] = event_title
                    event_list.append(event)
            except NoSuchElementException:
                is_search_result = False
                is_end = True

    finally:
        driver.quit()


    return event_list            