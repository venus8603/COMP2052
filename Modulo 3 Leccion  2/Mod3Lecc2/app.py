from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, identity_changed, identity_loaded, RoleNeed, UserNeed, Permission
from forms import LoginForm
from models import users

app = Flask(__name__)
app.secret_key = 'clave_autorizacion'

# Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Flask-Principal
principals = Principal(app)

# Permisos
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if str(user.id) == str(user_id):
            return user
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.role))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users.get(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        flash('Credenciales inválidas', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Bienvenido/a, {current_user.username}. Rol: {current_user.role}'

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin_area():
    return 'Área solo para administradores.'

@app.route('/editor')
@login_required
@editor_permission.require(http_exception=403)
def editor_area():
    return 'Área de edición para editores.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('login'))

@app.errorhandler(403)
def forbidden(e):
    return 'Acceso denegado: No tienes permiso para ver esta página.', 403

if __name__ == '__main__':
    app.run(debug=True)
