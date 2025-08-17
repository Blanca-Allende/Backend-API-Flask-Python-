from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Permitir solo tu dominio público de GitHub Pages
CORS(app, origins=["https://blanca-allende.github.io"])

@app.route("/")
def home():
    return jsonify({"message": "Servidor Flask corriendo 🚀 - usa /phi4 para probar el modelo"})

@app.route("/phi4", methods=["POST"])
def phi4():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    # Aquí podrías procesar la solicitud con tu modelo
    return jsonify({"message": f"Hola desde phi4! Recibí: {user_prompt}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



