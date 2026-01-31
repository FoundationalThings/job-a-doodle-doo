def format_email(jobs_by_company):
    """
    jobs_by_company: list of dicts like
    [
        {"company": "Home Depot", "jobs": [{"title": ..., "link": ..., "location": ...}, ...]},
        ...
    ]
    """
    lines = []
    for entry in jobs_by_company:
        lines.append(f"\n=== {entry['company']} ===")
        for job in entry["jobs"]:
            lines.append(f"- {job['title']} → {job['link']} ({job['location']})")
    return "\n".join(lines)
