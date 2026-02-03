from .base_extractor import run_extractor

def parse_ups_jobs(page):
    
    # Further filter needed to refine radius manually
    
    # slider = page.get_by_role("slider", name="location range")
    
    # slider.evaluate("el => { el.value = 30; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }")

    # await slider.fill("30")
    # await slider.dispatch_event("change")
    
    # Job listings
    
    jobs = []
    job_cards = page.locator('[data-ph-at-id="jobs-list-item"]')
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator('[data-ph-at-id="job-link"]').inner_text()
        link = card.locator('[data-ph-at-id="job-link"]').get_attribute("href")
        location = card.locator('[data-ph-at-id="job-info"]').nth(1).inner_text()
        
        if len(location.strip())== 0:
            location = "Various locations"
        
        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_ups_jobs,
        cookie_button_name="Essential Cookies Only",
        main_selector=".results-state",
        headless=True
    )