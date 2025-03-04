from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TND_TO_EUR_RATE = 0.30

@app.route('/')
def home():
    return "Bienvenue sur l'API de conversion TND -> EUR ! Utilisez /convert?amount=100"

@app.route('/convert', methods=['GET'])
def convert():
    amount = request.args.get('amount')
    if not amount:
        return jsonify({"error": "Le paramètre 'amount' est requis"}), 400
    try:
        amount = float(amount)
        if amount < 0:
            return jsonify({"error": "Le montant doit être positif"}), 400
    except ValueError:
        return jsonify({"error": "Le montant doit être un nombre valide"}), 400
    converted_amount = amount * TND_TO_EUR_RATE
    return jsonify({
        "amount_tnd": amount,
        "amount_eur": converted_amount,
        "exchange_rate": TND_TO_EUR_RATE
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
