from fastapi import FastAPI
from analyzer.whois_lookup import check_domain_age
from analyzer.vt_lookup import check_domain
from analyzer.scraper import fetch_page
from analyzer.ai_analysis import analyze_domain

app = FastAPI()

@app.get("/analyze")
def analyze(domain: str):

    whois_data = check_domain_age(domain)

    vt = check_domain(domain)

    page = fetch_page(domain)

    results = {
        "domain": domain,
        "whois": whois_data,
        "virustotal": vt,
        "page_data": page
    }

    ai_result = analyze_domain(results)

    return {
        "analysis": ai_result,
        "raw_data": results
    }
