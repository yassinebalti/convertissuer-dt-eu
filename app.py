from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

API_KEY = "34be5afffff4efecd3851e8d"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/TND"

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

    # Récupérer le taux de change actuel depuis l'API
    try:
        response = requests.get(API_URL)
        data = response.json()
        TND_TO_EUR_RATE = data['conversion_rates']['EUR']
    except Exception as e:
        return jsonify({"error": "Erreur lors de la récupération du taux de change", "details": str(e)}), 500

    converted_amount = amount * TND_TO_EUR_RATE

    # Obtenir la date et l'heure actuelles
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return jsonify({
        "amount_tnd": amount,
        "amount_eur": converted_amount,
        "exchange_rate": TND_TO_EUR_RATE,
        "conversion_time": current_time
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
