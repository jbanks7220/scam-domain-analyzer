import whois
from datetime import datetime

def check_domain_age(domain):
    data = whois.whois(domain)

    creation_date = data.creation_date

    if isinstance(creation_date, list):
        creation_date = creation_date[0]

    age_days = (datetime.now() - creation_date).days

    return {
        "creation_date": str(creation_date),
        "age_days": age_days
    }
