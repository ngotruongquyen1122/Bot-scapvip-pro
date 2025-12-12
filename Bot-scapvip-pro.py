from flask import Flask, request
import requests, os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    msg = f"""
🛰 <b>CB-Scalp Pro Signal</b>

<b>Symbol:</b> {data.get("symbol")}
<b>Timeframe:</b> {data.get("tf")}
<b>Signal:</b> {data.get("side")}

🎯 Entry: {data.get("entry")}
🛑 SL: {data.get("sl")}
🎯 TP1: {data.get("tp1")}
🎯 TP2: {data.get("tp2")}
"""
    send_telegram(msg)
    return {"ok": True}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
