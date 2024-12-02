import requests
from pathlib import Path

# Define the directory for output files and ensure it exists
output_dir = Path("ts")
output_dir.mkdir(parents=True, exist_ok=True)

# Read URLs from file
with open('ts.txt', 'r') as f:
	ts_urls = [line.strip() for line in f]

# Download and save each file
for num, url in enumerate(ts_urls, start=1):
	try:
		print(f"Downloading {url}...")
		response = requests.get(url)
		response.raise_for_status()  # Raise HTTPError for bad responses
		
		ts_name = output_dir / f"{str(num).zfill(3)}.ts"  # e.g., "001.ts"
		with ts_name.open('wb') as ts_file:
			ts_file.write(response.content)
		print(f"Saved: {ts_name}")
	except requests.RequestException as e:
		print(f"Error downloading {url}: {e}")
