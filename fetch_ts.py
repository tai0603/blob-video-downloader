# Path to the M3U8 file
m3u8_file = ""

# Output file to save .ts URLs
output_file = ""

# Read the M3U8 file and extract .ts URLs
ts_urls = []
with open(m3u8_file, 'r') as file:
	for line in file:
		line = line.strip()
		if line.endswith(".ts"): # Check if the line ends with .ts
			ts_urls.append(line)

# Write the extracted URLs to an output file
with open(output_file, 'w') as out_file:
	out_file.write("\n".join(ts_urls))

print(f"Extracted {len(ts_urls)} .ts URLs and saved to {output_file}")
