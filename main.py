from playwright.sync_api import sync_playwright
from launcher import browser_trigger as bt
import time

QUERY = "site:myshopify.com clothing"

def site_crawling(query):

    p, browser, context, page = bt("https://www.google.com")

    page.wait_for_load_state("domcontentloaded")
    
    search_box = page.wait_for_selector('[name="q"]') # wait for search box
    search_box.click()
    
    page.keyboard.type(query, delay=20)
    page.keyboard.press("Enter")
    time.sleep(20)      

    browser.close()
    p.stop()


site_crawling(query=QUERY)