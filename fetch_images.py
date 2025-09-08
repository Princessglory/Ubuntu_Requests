import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check if response is an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped {url}: Not an image (Content-Type: {content_type})")
            return

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Save path
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        if os.path.exists(filepath):
            print(f"⚠ Skipped {filename}: already exists.")
            return

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred while saving {url}: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs
    urls = input("Enter one or more image URLs (separated by spaces): ").split()

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Process each URL
    for url in urls:
        fetch_image(url)

    print("\n✨ Done! Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
