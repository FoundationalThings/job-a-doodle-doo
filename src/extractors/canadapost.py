from .base_extractor import run_extractor

BASE_URL = "https://jobs.canadapost.ca"

def parse_canadapost_jobs(page):
    jobs = []
    
    if page.locator("#attention").count() > 0:
        print("Canada Post: No jobs found.")
        return jobs
    
    job_cards = page.locator("li.job-tile")
    
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator("a.jobTitle-link").first.inner_text()
        
        link = card.locator("a.jobTitle-link").first.get_attribute("href")
        if link and not link.startswith("http"):
            link = BASE_URL + link
            
        location = card.locator("div[id$='-section-city-value']").first.inner_text()
        
        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })    
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_canadapost_jobs,
        cookie_button_name="Accept All",
        main_selector="#content"
    )
    
    