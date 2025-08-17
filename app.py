from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/phi4", methods=["POST"])
def phi4():
    data = request.get_json()
    mensaje = data.get("prompt", "")
    
    # Aquí podrías integrar tu modelo real
    # Por ahora devolvemos un texto simulado
    respuesta = f"🤖 Simulación de phi4: {mensaje}"
    
    return jsonify({"response": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Render necesita host 0.0.0.0
