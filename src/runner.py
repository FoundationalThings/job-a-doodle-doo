from extractors import homedepot, fedex

EXTRACTORS = {
    "Home Depot": homedepot,
    "FedEx": fedex,
}

import email_formatter
import os
from sheets import load_targets
from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
from email_sender import send_email


RECIPIENT_EMAIL_ADDRESSES = os.environ.get("RECIPIENT_EMAIL_ADDRESSES")



def generate_email_subject():
    """Create a subject line with the current date."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M")
    return f"Job-a-Doodle-Doo: New Jobs as of {date_str}"

def generate_email_timestamp():
    """Return a readable timestamp for the email footer."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y at %I:%M %p")




def main():    
    SHEET_ID = os.environ["SHEET_ID"]
    targets = load_targets(SHEET_ID)

    email_content = []

    all_jobs = []
    jobs = []
    
    print("Starting job extraction...")

    for target in targets:
        print(f"Fetching jobs for {target['company']} from {target['url']}...")
        extractor = EXTRACTORS.get(target["company"])
        if extractor:
            jobs = extractor.fetch_jobs(target["url"])
            
            email_content.append({
                "company": target["company"],
                "company_jobs_url": target['url'],
                "jobs": jobs
            })            
                  
            all_jobs.extend(jobs)


    print(f"Total jobs found: {len(all_jobs)}")
    
    

    subject = generate_email_subject()
    timestamp = generate_email_timestamp()
    html_body = email_formatter.format_email_html(email_content, timestamp)
    send_email(subject, html_body, RECIPIENT_EMAIL_ADDRESSES.split(","))

if __name__ == "__main__":
    main()