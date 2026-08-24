import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
LOCAL_API_URL = "http://localhost:8000/api/orders"
REQUEST_TIMEOUT = 20
OUTPUT_FILE = Path("data/raw/api_snapshot.json")
EVIDENCE_FILE = Path("data/evidence/api_inspection.txt")

def try_api(url):
    print(f"\nTrying API: {url}")
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        return response
    except requests.exceptions.ConnectionError:
        print(f"Connection failed to {url}")
        return None
    except requests.exceptions.Timeout:
        print(f"Timeout for {url}")
        return None

def inspect_api():
    print("\n" + "=" * 80)
    print("DSS150P LAB 01 - REST API INSPECTION")
    print("=" * 80)
    
    start_time = datetime.now(timezone.utc)
    print(f"\nInspection started at (UTC): {start_time.isoformat()}")
    print(f"Timeout: {REQUEST_TIMEOUT} seconds")
    
    response = try_api(API_URL)
    used_url = API_URL
    
    if response is None or response.status_code != 200:
        print(f"\nPublic API failed, trying local API...")
        response = try_api(LOCAL_API_URL)
        used_url = LOCAL_API_URL
    
    if response is None:
        print("\nBoth APIs failed!")
        print("Please run: python src/local_api_server.py")
        print("Then try again.")
        sys.exit(1)
    
    print(f"\nUsing API: {used_url}")
    print(f"HTTP Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response body: {response.text[:500]}")
        sys.exit(1)
    
    content_type = response.headers.get("Content-Type", "Not specified")
    print(f"Content-Type: {content_type}")
    
    print("\nParsing JSON response...")
    try:
        payload = response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        print(f"Response content preview:")
        print(response.text[:500])
        sys.exit(1)
    
    print(f"\nTop-level JSON structure: {type(payload).__name__}")
    
    if isinstance(payload, list):
        print(f"Number of records: {len(payload)}")
    elif isinstance(payload, dict):
        print(f"Top-level keys: {list(payload.keys())}")
        for key, value in payload.items():
            if isinstance(value, list):
                print(f"Number of records in '{key}': {len(value)}")
            elif isinstance(value, dict):
                print(f"'{key}' contains keys: {list(value.keys())}")
    
    print("\nSample record:")
    if isinstance(payload, list) and len(payload) > 0:
        print(json.dumps(payload[0], indent=2, ensure_ascii=False)[:1000])
    elif isinstance(payload, dict):
        for key, value in payload.items():
            if isinstance(value, list) and len(value) > 0:
                print(f"From '{key}':")
                print(json.dumps(value[0], indent=2, ensure_ascii=False)[:1000])
                break
        else:
            sample = {k: payload[k] for k in list(payload.keys())[:3]}
            print(json.dumps(sample, indent=2, ensure_ascii=False)[:1000])
    
    print(f"\nSaving snapshot to: {OUTPUT_FILE}")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    
    print(f"Snapshot saved successfully")
    print(f"File size: {OUTPUT_FILE.stat().st_size:,} bytes")
    
    end_time = datetime.now(timezone.utc)
    retrieval_timestamp = end_time.isoformat()
    print(f"\nRetrieved at (UTC): {retrieval_timestamp}")
    
    EVIDENCE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(EVIDENCE_FILE, "w", encoding="utf-8") as f:
        f.write("=== API INSPECTION EVIDENCE ===\n")
        f.write(f"Retrieved at (UTC): {retrieval_timestamp}\n")
        f.write(f"API URL: {used_url}\n")
        f.write(f"HTTP Status: {response.status_code}\n")
        f.write(f"Content-Type: {content_type}\n")
        f.write(f"Top-level type: {type(payload).__name__}\n")
        if isinstance(payload, list):
            f.write(f"Number of records: {len(payload)}\n")
        f.write(f"Snapshot file: {OUTPUT_FILE}\n")
    
    print(f"Evidence saved to: {EVIDENCE_FILE}")
    print(f"\nInspection completed at (UTC): {end_time.isoformat()}")
    
    return retrieval_timestamp

if __name__ == "__main__":
    inspect_api()