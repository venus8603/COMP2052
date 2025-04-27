from flask import Flask, render_template, redirect, flash, url_for
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'secreto_super_secreto'  # Necesario para CSRF y mensajes flash

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Usuario {form.name.data} registrado con éxito', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
