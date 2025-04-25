from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de usuarios en memoria
usuarios = {"usuarios": []}

@app.route("/", methods=["GET"])
def home():
    return "API de gestión de usuarios"

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "mensaje": "Sistema de gestión de usuarios",
        "version": "1.0",
        "autor": "Tu Nombre"
    })

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json

    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({"error": "Datos incompletos: se requiere 'nombre' y 'correo'."}), 400

    nuevo_usuario = {
        "id": len(usuarios["usuarios"]) + 1,
        "nombre": data["nombre"],
        "correo": data["correo"]
    }
    
    usuarios["usuarios"].append(nuevo_usuario)

    return jsonify({"mensaje": "Usuario creado exitosamente.", "usuario": nuevo_usuario})

if __name__ == "__main__":
    app.run(debug=True)
