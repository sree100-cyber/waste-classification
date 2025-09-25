# download_sample_waste_images_windows.py

import os
import requests

# Sample image URLs from Wikimedia Commons (public domain)
categories = {
    "Plastic": [
        "https://upload.wikimedia.org/wikipedia/commons/7/7e/Plastic_bottle.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/6/6e/Plastic_bags.jpg"
    ],
    "Paper": [
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/Paper_waste.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/8/84/Newspaper_stack.jpg"
    ],
    "Glass": [
        "https://upload.wikimedia.org/wikipedia/commons/2/2d/Glass_bottles.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/f/f3/Glass_jars.jpg"
    ],
    "Metal": [
        "https://upload.wikimedia.org/wikipedia/commons/5/50/Aluminium_cans.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/49/Metal_scrap.jpg"
    ],
    "Organic": [
        "https://upload.wikimedia.org/wikipedia/commons/f/fb/Organic_waste.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/Food_waste.jpg"
    ]
}

# Create dataset folders
os.makedirs("dataset", exist_ok=True)

for category, urls in categories.items():
    category_path = os.path.join("dataset", category)
    os.makedirs(category_path, exist_ok=True)

    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise error if failed
            file_path = os.path.join(category_path, f"{category.lower()}{i+1}.jpg")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {file_path}")
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")
