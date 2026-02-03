from .base_extractor import run_extractor

BASE_URL = "https://careers.fedex.com"

def parse_fedex_jobs(page):
    jobs = []
    job_cards = page.locator(".results-list__item")
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator(".results-list__item-title").inner_text()
        link = card.locator("a.results-list__item-title--link").get_attribute("href")
        if link and not link.startswith("http"):
            link = BASE_URL + link
        location = card.locator(".results-list__item-street--label").inner_text()
        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_fedex_jobs,
        cookie_button_name="Accept All",
        main_selector=".results-list"
    )