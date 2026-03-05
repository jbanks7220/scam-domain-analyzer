import requests

API_KEY = "YOUR_VT_API_KEY"

def check_domain(domain):

    url = f"https://www.virustotal.com/api/v3/domains/{domain}"

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    return stats
