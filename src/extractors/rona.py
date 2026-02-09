from .base_extractor import run_extractor

BASE_URL = "https://jobs.ronainc.ca"

def parse_rona_jobs(page):
    jobs = []
    job_cards = page.locator("div.flex.flex-col.gap-6.border.p-6")
    
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator("a.text-xl.font-black.uppercase.text-black").inner_text()
        
        link = card.locator("a.text-xl.font-black.uppercase.text-black").get_attribute("href")
        if link and not link.startswith("http"):
            link = BASE_URL + link
            
        location = card.locator("div.flex.flex-row.items-center.text-black span.ml-2").inner_text()
        
        jobs.append({
            "title": title,
            "link": link,
            "location": location
        })
    return jobs

def fetch_jobs(url):
    return run_extractor(
        url,
        parse_rona_jobs,
        cookie_button_name="Allow Essential Cookies",
        main_selector="#locations-map > div:nth-child(2) > section > div > div.h-fit.w-full.rounded-lg.bg-white.p-6 > div.flex.flex-col.gap-6.text-\[16px\]"
    )
    
    