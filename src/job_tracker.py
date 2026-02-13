def save_links_to_file(all_jobs, filename):
    with open(filename, "w") as f:
        for job in all_jobs:
            f.write(job['link'] + "\n")
            