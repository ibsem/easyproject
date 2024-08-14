from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import Projeto, Usuario

bp = Blueprint('projetos', __name__)

@bp.route('/projetos')
def listar_projetos():
    projetos = Projeto.query.all()
    return render_template('projeto_list.html', projetos=projetos)

@bp.route('/projetos/novo', methods=['GET', 'POST'])
def criar_projeto():
    if request.method == 'POST':
        nome_projeto = request.form['nome_projeto']
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_termino = request.form.get('data_termino')
        usuario_responsavel_id = request.form['usuario_responsavel_id']
        projeto = Projeto(nome_projeto=nome_projeto, descricao=descricao, data_inicio=data_inicio,
                          data_termino=data_termino, usuario_responsavel_id=usuario_responsavel_id)
        db.session.add(projeto)
        db.session.commit()
        return redirect(url_for('projetos.listar_projetos'))
    usuarios = Usuario.query.all()
    return render_template('projeto_form.html', usuarios=usuarios)

@bp.route('/projetos/<int:projeto_id>/editar', methods=['GET', 'POST'])
def atualizar_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    if request.method == 'POST':
        projeto.nome_projeto = request.form['nome_projeto']
        projeto.descricao = request.form['descricao']
        projeto.data_inicio = request.form['data_inicio']
        projeto.data_termino = request.form.get('data_termino')
        projeto.usuario_responsavel_id = request.form['usuario_responsavel_id']
        db.session.commit()
        return redirect(url_for('projetos.listar_projetos'))
    usuarios = Usuario.query.all()
    return render_template('projeto_form.html', projeto=projeto, usuarios=usuarios)

@bp.route('/projetos/<int:projeto_id>/deletar')
def deletar_projeto(projeto_id):
    projeto = Projeto.query.get_or_404(projeto_id)
    db.session.delete(projeto)
    db.session.commit()
    return redirect(url_for('projetos.listar_projetos'))
