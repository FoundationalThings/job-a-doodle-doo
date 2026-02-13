def save_links_to_file(all_jobs, filename):
    with open(filename, "w") as f:
        for job in all_jobs:
            f.write(job['link'] + "\n")
            
            
def load_links_from_file(filename):
    with open(filename, "r") as f:
        return set(line.strip() for line in f.readlines())
    
