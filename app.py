from flask import Flask, request, render_template
from config import get_tenant
from services.ai import ai_reply
from services.whatsapp import send_text
from memory.users import get_user
from utils.rate_limit import is_spam

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    msg = data["entry"][0]["changes"][0]["value"]["messages"][0]

    phone = msg["from"]
    phone_number_id = data["entry"][0]["changes"][0]["value"]["metadata"]["phone_number_id"]

    tenant = get_tenant(phone_number_id)
    if not tenant or is_spam(phone):
        return "OK", 200

    user = get_user(phone)
    text = msg["text"]["body"]

    ai_res = ai_reply(text, user)
    send_text(tenant, phone, ai_res["message"])

    if "order_data" in ai_res:
        user.update(ai_res["order_data"])

    return "OK", 200


@app.route("/admin/orders")
def admin_orders():
    return "Admin Panel Ready ✅"

if __name__ == "__main__":
    app.run(port=3000)

