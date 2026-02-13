from extractors import homedepot, fedex, ups, rona, purolator, canadapost

EXTRACTORS = {
    "Home Depot": homedepot,
    "FedEx": fedex,
    "UPS": ups,
    "RONA": rona,
    "Purolator": purolator,
    "Canada Post": canadapost
}

import email_formatter
from email_sender import send_email
from job_tracker import save_links_to_file

import os
from sheets import load_targets
from dotenv import load_dotenv
load_dotenv()



RECIPIENT_EMAIL_ADDRESSES = os.environ.get("RECIPIENT_EMAIL_ADDRESSES")

def main():    
    SHEET_ID = os.environ["SHEET_ID"]
    targets = load_targets(SHEET_ID)

    email_content = []

    all_jobs = []
    jobs = []
    
    print("Starting job extraction...")

    for target in targets:
        print(f"Fetching jobs for {target['company']} from {target['url']}...")
        
        extractor = None
        for key in EXTRACTORS:
            if target["company"].startswith(key):
                extractor = EXTRACTORS[key]
                break

        if extractor:
            jobs = extractor.fetch_jobs(target["url"])
            
            email_content.append({
                "company": target["company"],
                "company_jobs_url": target['url'],
                "jobs": jobs
            })            
                  
            all_jobs.extend(jobs)


    print(f"Total jobs found: {len(all_jobs)}")
    
    subject = email_formatter.generate_email_subject()
    html_body = email_formatter.format_email_html(email_content)
    # send_email(subject, html_body, RECIPIENT_EMAIL_ADDRESSES.split(","))
    save_links_to_file(all_jobs, "job_links.txt")

if __name__ == "__main__":
    main()