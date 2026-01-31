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

def main():    
    sheet_id = os.environ["SHEET_ID"]
    targets = load_targets(sheet_id)

    email_content = []

    all_jobs = []
    jobs = []
    
    print("Starting job extraction...")

    for target in targets:
        extractor = EXTRACTORS.get(target["company"])
        if extractor:
            jobs = extractor.fetch_jobs(target["url"])
            
            email_content.append({
                "company": target["company"],
                "jobs": jobs
            })            
                  
            all_jobs.extend(jobs)


    print(f"Total jobs found: {len(all_jobs)}")
    print(f"Email content prepared for {len(email_content)} companies.")
    print(f"Email content: {email_content}")
    
    formatted_email = email_formatter.format_email(email_content)
    print("Formatted Email Content:")
    print(formatted_email)
    
if __name__ == "__main__":
    main()