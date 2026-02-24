from playwright.sync_api import sync_playwright
from launcher import browser_trigger as bt
import time

def site_crawling(query):
    p, browser, context, page = bt("https://www.google.com")
    
    # Search for the sites
    page.click("input[names=q]")
    page.keyboard.type(query, delay=100)
    page.keyboard.press('Enter')  
    browser.close()
    p.stop()
    

site_crawling()
