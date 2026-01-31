import os
from sheets import load_targets
from dotenv import load_dotenv

load_dotenv()

def main():
    sheet_id = os.environ["SHEET_ID"]
    targets = load_targets(sheet_id)

    print(f"Found {len(targets)} enabled targets:")
    for t in targets:
        print("-", t)

if __name__ == "__main__":
    main()
