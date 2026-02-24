from playwright.sync_api import sync_playwright

def browser_trigger(url):
    """This function helps on the process of launching a browser"""
    p = sync_playwright().start()
    browser = p.firefox.launch(headless=False)
    context = browser.new_context(    
        viewport={"width": 1250, "height": 881},    
        ignore_https_errors=False,
        bypass_csp=False,
        user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0' # FIREFOX UA
        #user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36", # CHROME UA
        timezone_id="Africa/Nairobi",    
        geolocation={
            "latitude": -1.286389,
            "longitude": 36.817223,
            "accuracy": 100
        },
        permissions=["geolocation"],
        # --- Headers ---
        extra_http_headers={
            "Accept-Language": "en-KE,en;q=0.9",
            "Upgrade-Insecure-Requests": "1"
        },    
        offline=False,
        http_credentials={
            "username": "user",
            "password": "pass"
        },    
        device_scale_factor=1,
        is_mobile=False,
        has_touch=False,
        color_scheme="light",            # "light" | "dark" | "no-preference"
        reduced_motion="no-preference",  # "reduce" | "no-preference"
        forced_colors="none",            # replaces "contrast"    
        accept_downloads=True,    
        #record_har_path="network.har",    
        service_workers="allow",         # "allow" | "block"    
        )

    page = context.new_page()
    page.goto(url, timeout=750000)
    
    return p, browser, context, page

if __name__ == "__main__":
    browser_trigger()