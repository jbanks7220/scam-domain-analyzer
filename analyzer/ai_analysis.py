from openai import OpenAI

client = OpenAI()

def analyze_domain(domain_data):

    prompt = f"""
    Analyze the following website indicators and determine phishing risk.

    Data:
    {domain_data}

    Output:
    Risk level (LOW/MEDIUM/HIGH)
    Key indicators
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
