import requests, os, json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
أنت مندوب مبيعات مصري محترف.
اسأل سؤال واحد في كل رسالة.
لهجة مصرية محترمة.
هدفك إتمام البيع.
الرد دايمًا JSON.
"""

def ai_reply(message, memory):
    payload = {
        "model": "gpt-4.1-mini",
        "response_format": {"type": "json_object"},
        "input": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
رسالة العميل:
{message}

بيانات معروفة:
{json.dumps(memory, ensure_ascii=False)}
"""
            }
        ]
    }

    r = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    return json.loads(r.json()["output_text"])
