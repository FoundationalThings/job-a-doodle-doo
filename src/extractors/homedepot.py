from .base_extractor import run_extractor

def parse_homedepot_jobs(page):
    jobs = []
    job_cards = page.locator("#job-list-items > li > a.job-link")
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        link = card.get_attribute("href")
        title = card.locator("div.job-title").inner_text()
        location = card.locator("div.job-location").inner_text()

        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_homedepot_jobs,
        cookie_button_name="Accept All",
        main_selector="#job-list-items"
    )