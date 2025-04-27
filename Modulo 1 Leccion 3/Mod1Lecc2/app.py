from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'sistema': 'Gestión de Usuarios y Productos',
        'version': '1.0',
        'autor': 'Tu Nombre'
    }), 200

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if not data or 'nombre' not in data or 'correo' not in data:
        return jsonify({'error': 'Faltan datos requeridos (nombre y correo).'}), 400

    usuario = {
        'nombre': data['nombre'],
        'correo': data['correo']
    }
    usuarios.append(usuario)
    return jsonify({'mensaje': 'Usuario creado exitosamente.', 'usuario': usuario}), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({'usuarios': usuarios}), 200

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return jsonify({'error': 'Ruta no encontrada.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
