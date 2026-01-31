from playwright.sync_api import sync_playwright, TimeoutError

BASE_URL = "https://careers.fedex.com/"

def fetch_jobs(url):
    
    print(f"Fetching jobs from {url}...")
    
    """Fetch Home Depot jobs from a given URL."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        # Navigate to the jobs page
        page.goto(url)

        # Optional: dismiss cookies popup if it exists
        try:
            page.get_by_role("button", name="Accept All").click(timeout=2000)
            print("Cookies popup dismissed")
        except TimeoutError:
            # Button didn't appear — that's fine
            print("No cookies popup found, continuing")
            pass

        # Now wait for the job list
        page.wait_for_selector(".results-list")
        print("Page ready")

        # Extract jobs
        jobs = []
        # job_cards = page.locator("#job-list-items")  # adjust to actual job card locator
        job_cards = page.locator("ul#job-list-items > li > a.job-link")  # Home Depot job
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
        

        browser.close()
        
        print(f"Found {len(jobs)} jobs.")
        
        
        return jobs
