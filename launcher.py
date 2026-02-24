from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync   # <-- ADD THIS

def browser_trigger(url):
    p = sync_playwright().start()
    browser = p.firefox.launch(headless=False)
    
    context = browser.new_context(    
        viewport={"width": 1920, "height": 1080},  # more normal size
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0',
        timezone_id="Africa/Nairobi",    
        geolocation={"latitude": -1.286389, "longitude": 36.817223, "accuracy": 100},
        permissions=["geolocation"],
        extra_http_headers={
            "Accept-Language": "en-KE,en;q=0.9",
            "Upgrade-Insecure-Requests": "1"
        },
        # REMOVE the http_credentials block entirely
        # accept_downloads=True, etc. keep what you need
    )
   
    page = context.new_page()
    stealth_sync(page)   # <-- THIS IS THE MAGIC LINE
    
    page.goto(url, timeout=750000)
    return p, browser, context, page