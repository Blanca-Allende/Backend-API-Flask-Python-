from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Permitir cualquier origen
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return jsonify({"message": "Servidor Flask corriendo 🚀 - usa /phi4 para probar el modelo"})

@app.route("/phi4", methods=["POST", "OPTIONS"])
def phi4():
    if request.method == "OPTIONS":
        # Responder preflight request
        response = app.make_response('')
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response

    data = request.get_json()
    prompt = data.get("prompt", "")
    return jsonify({"message": f"Hola desde phi4! Recibí tu prompt: {prompt}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


