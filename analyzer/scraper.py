import requests
from bs4 import BeautifulSoup

def fetch_page(domain):

    url = f"http://{domain}"

    r = requests.get(url, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text()

    forms = soup.find_all("form")

    return {
        "text_sample": text[:2000],
        "forms_detected": len(forms)
    }
