import json

def save_jobs_to_file(all_jobs, filename):
    with open(filename, "w") as f:
        json.dump(all_jobs, f)

def load_jobs_from_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

