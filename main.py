
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(
    url,
    timeout=20,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text(strip=True))
