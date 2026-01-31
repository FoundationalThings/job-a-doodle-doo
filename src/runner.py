from extractors import homedepot, fedex

import os
from sheets import load_targets
from dotenv import load_dotenv

load_dotenv()
def main():    
    sheet_id = os.environ["SHEET_ID"]
    targets = load_targets(sheet_id)

    all_jobs = []
    jobs = []
    
    print("Starting job extraction...")

    for target in targets:
        if target['company'] == 'Home Depot':
            jobs = homedepot.fetch_jobs(target['url'])
        elif target['company'] == 'FedEx':
            jobs = fedex.fetch_jobs(target['url'])    
            
        all_jobs.extend(jobs)

    # Do something with jobs, e.g., print or write to Sheet
    for job in all_jobs:
        print(job)


    print(f"Total jobs found: {len(all_jobs)}")
    
    
if __name__ == "__main__":
    main()