from .base_extractor import run_extractor

BASE_URL = "https://careers.purolator.com"

def parse_purolator_jobs(page):
    jobs = []
    job_cards = page.locator("tr.data-row")
    
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator("a.jobTitle-link").first.inner_text()
        
        link = card.locator("a.jobTitle-link").first.get_attribute("href")
        if link and not link.startswith("http"):
            link = BASE_URL + link
            
        location = card.locator(".jobLocation").first.inner_text()
        
        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_purolator_jobs,
        cookie_button_name="Accept",
        main_selector="#searchresults"
    )
    
    