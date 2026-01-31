from googleapiclient.discovery import build
from google.auth import default

SHEET_RANGE = "Sheet1!A2:C"  # A: enabled, B: company, C: URL

def load_targets(sheet_id):
    creds, _ = default()

    service = build("sheets", "v4", credentials=creds)

    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=SHEET_RANGE
    ).execute()

    rows = result.get("values", [])

    targets = []
    for row in rows:
        if len(row) < 3:
            continue

        enabled, company, url = row

        if enabled.strip().lower() in ("yes", "y", "true", "1"):
            targets.append({
                "company": company,
                "url": url
            })

    return targets
