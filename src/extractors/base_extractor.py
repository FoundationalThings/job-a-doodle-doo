from playwright.sync_api import sync_playwright, TimeoutError

def run_extractor(
    url,
    parse_func,
    cookie_button_name="Accept All",
    main_selector=None,
    headless=True
):
    print(f"Fetching jobs from {url}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(url)
        try:
            page.get_by_role("button", name=cookie_button_name).click(timeout=2000)
            print("Cookies popup dismissed")
        except TimeoutError:
            print("No cookies popup found, continuing")
        if main_selector:
            page.wait_for_selector(main_selector)
            print("Page ready")
        jobs = parse_func(page)
        browser.close()
        print(f"Found {len(jobs)} jobs.")
        return jobs