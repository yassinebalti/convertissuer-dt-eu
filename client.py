import requests

while True:
    try:
        montant = float(input("Entrez le montant en TND (ou 0 pour quitter) : "))
        if montant == 0:
            print("Au revoir !")
            break

        # Appel à l'API Flask
        response = requests.get(f"http://127.0.0.1:5000/convert?amount={montant}")
        data = response.json()

        if response.status_code == 200:
            print(f"{data['amount_tnd']} TND = {data['amount_eur']} EUR (Taux: {data['exchange_rate']})")
        else:
            print("Erreur :", data.get("error", "Erreur inconnue"))

    except ValueError:
        print("Veuillez entrer un nombre valide.")
    except Exception as e:
        print("Erreur lors de l'appel à l'API :", e)
