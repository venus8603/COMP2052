from flask import Flask, render_template

app = Flask(__name__)

productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor']
usuarios = ['Ana', 'Luis', 'María', 'Carlos']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def lista_productos():
    return render_template('productos.html', productos=productos)

@app.route('/usuarios')
def lista_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
