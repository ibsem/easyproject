from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app import db
from models import Usuario

bp = Blueprint('usuarios', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form['login']
        senha_input = request.form['senha']
        usuario = Usuario.query.filter_by(login=login_input).first()
        if usuario and usuario.senha == senha_input:
            login_user(usuario)
            return redirect(url_for('projetos.listar_projetos'))
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
