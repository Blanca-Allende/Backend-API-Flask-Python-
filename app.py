import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return jsonify({"message": "Servidor Flask corriendo 🚀 - usa /phi4 para probar el modelo"})

@app.route("/phi4", methods=["POST"])
def phi4():
    return jsonify({"message": "Hola desde phi4!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


