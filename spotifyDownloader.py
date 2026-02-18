import time
import requests
import json
import re
from tqdm import tqdm

# === Configuration ===
API_TOKEN = "MUSICFETCH_API_KEY"
INPUT_FILE = "SPOTIFY_LINK_LIST"
OUTPUT_FILE = "YOUTUBE_LINK_LIST"
SERVICES = ["spotify", "youtube"]
SLEEP_TIME = 1  # seconds between requests
MAX_RETRIES = 3  # number of retries for failed requests

# === Regex to match YouTube Music links ===
YTM_LINK_REGEX = re.compile(r"https://music\.youtube\.com/watch\?v=[\w-]+")

# === Read Spotify links from file ===
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spotify_links = [line.strip() for line in f if line.strip()]

youtube_links = []

# === Fetch YouTube Music links ===
for link in tqdm(spotify_links, desc="Fetching YouTube Music links"):
    params = {
        "url": link,
        "services": ",".join(SERVICES)
    }
    headers = {"x-token": API_TOKEN}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get("https://api.musicfetch.io/url", params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Search the JSON for YouTube Music links
            json_str = json.dumps(data)
            matches = YTM_LINK_REGEX.findall(json_str)

            if matches:
                youtube_links.append(matches[0])  # Take the first match only
            # If no match, skip

            break  # exit retry loop on success

        except requests.RequestException as e:
            if attempt < MAX_RETRIES:
                print(f"Retry {attempt}/{MAX_RETRIES} for {link}...")
                time.sleep(SLEEP_TIME)
            else:
                print(f"Failed to fetch {link}: {e}")

    time.sleep(SLEEP_TIME)

# === Save YouTube Music links to TXT ===
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for yt_link in youtube_links:
        f.write(yt_link + "\n")

print(f"\nYouTube Music links saved to {OUTPUT_FILE}")
