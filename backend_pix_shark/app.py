
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PAGARME_API_KEY = "sk_49db836e59424b29b28deb931ad31e38"

@app.route('/pix', methods=['POST'])
def criar_pix():
    data = request.json

    headers = {
        "Authorization": f"Bearer {PAGARME_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "amount": data.get("amount", 1000),  # em centavos
        "payment_method": "pix",
        "pix": {
            "expires_in": 3600
        },
        "customer": {
            "name": data.get("name", "Cliente"),
            "email": data.get("email", "cliente@email.com"),
            "tax_id": data.get("cpf", "12345678909"),
            "phones": {
                "mobile_phone": {
                    "country_code": "55",
                    "area_code": "11",
                    "number": "999999999"
                }
            }
        },
        "items": [
            {
                "name": data.get("item", "Proxy"),
                "quantity": 1,
                "unit_price": data.get("amount", 1000)
            }
        ]
    }

    try:
        response = requests.post(
            "https://api.pagar.me/core/v5/orders",
            headers=headers,
            json=payload
        )
        resp_json = response.json()
        pix_info = resp_json.get("charges", [])[0].get("last_transaction", {})
        return jsonify({
            "pixCode": pix_info.get("qr_code"),
            "qrUrl": pix_info.get("qr_code_url"),
            "transactionId": resp_json.get("id")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Backend Pix ativo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
