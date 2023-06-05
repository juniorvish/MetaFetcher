import requests
from bs4 import BeautifulSoup
import json

def fetch_metadata(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        metadata = {
            "title": get_title(soup),
            "description": get_description(soup),
            "image": get_image(soup),
            "url": url
        }

        return json.dumps(metadata)
    except Exception as e:
        return json.dumps({"error": str(e)})

def get_title(soup):
    title = soup.find("title")
    if title:
        return title.text
    else:
        return ""

def get_description(soup):
    description = soup.find("meta", attrs={"name": "description"})
    if description:
        return description.get("content", "")
    else:
        return ""

def get_image(soup):
    image = soup.find("meta", attrs={"property": "og:image"})
    if image:
        return image.get("content", "")
    else:
        return ""