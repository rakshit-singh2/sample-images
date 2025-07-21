# generate_metadata.py

import os
import json
import re

IMAGE_DIR = "."
METADATA_DIR = "metadata"
BASE_URL = "https://rakshit-singh2.github.io/sample-images"

# Make sure metadata folder exists
os.makedirs(METADATA_DIR, exist_ok=True)

# Regex to match files like image-1.jpg, image-23.jpg etc
pattern = re.compile(r"image-(\d+)\.jpg")

for filename in os.listdir(IMAGE_DIR):
    match = pattern.match(filename)
    if match:
        token_id = int(match.group(1))
        metadata = {
            "name": f"Metaverse NFT #{token_id}",
            "description": "A unique Metaverse asset representing creativity.",
            "image": f"{BASE_URL}/{filename}",
            "attributes": [
                {"trait_type": "Theme", "value": "Dynamic"},
                {"trait_type": "ID", "value": token_id}
            ]
        }

        json_path = os.path.join(METADATA_DIR, f"image-{token_id}.json")
        with open(json_path, "w") as f:
            json.dump(metadata, f, indent=4)

print("✅ Metadata generated successfully.")
