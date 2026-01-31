from playwright.sync_api import sync_playwright, TimeoutError

url = "https://careers.homedepot.ca/job-search?location=%5B%22ON%20-%20Cambridge%22%2C%22ON%20-%20Guelph%22%2C%22ON%20-%20Kitchener%22%2C%22ON%20-%20Orangeville%22%2C%22ON%20-%20Waterloo%22%5D"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(url)

    # Optional: dismiss cookies popup if it exists
    try:
        page.get_by_role("button", name="Accept All").click(timeout=2000)
        print("Cookies popup dismissed")
    except TimeoutError:
        # Button didn't appear — that's fine
        print("No cookies popup found, continuing")

    # Now wait for the job list
    page.wait_for_selector("#job-list-items")
    print("Page ready")
    
    browser.close()
