from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from models import Sprint, Projeto, Usuario

bp = Blueprint('sprints', __name__)

@bp.route('/sprints/<int:projeto_id>')
def listar_sprints(projeto_id):
    sprints = Sprint.query.filter_by(projeto_id=projeto_id).all()
    return render_template('sprint_list.html', sprints=sprints, projeto_id=projeto_id)

@bp.route('/sprints/novo/<int:projeto_id>', methods=['GET', 'POST'])
def criar_sprint(projeto_id):
    if request.method == 'POST':
        nome_sprint = request.form['nome_sprint']
        descricao = request.form['descricao']
        data_inicio = request.form['data_inicio']
        data_termino = request.form.get('data_termino')
        status = request.form['status']
        responsavel_id = request.form['responsavel_id']
        sprint = Sprint(projeto_id=projeto_id, nome_sprint=nome_sprint, descricao=descricao,
                        data_inicio=data_inicio, data_termino=data_termino, status=status,
                        responsavel_id=responsavel_id)
        db.session.add(sprint)
        db.session.commit()
        return redirect(url_for('sprints.listar_sprints', projeto_id=projeto_id))
    usuarios = Usuario.query.all()
    return render_template('sprint_form.html', projeto_id=projeto_id, usuarios=usuarios)

@bp.route('/sprints/<int:sprint_id>/editar', methods=['GET', 'POST'])
def atualizar_sprint(sprint_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    if request.method == 'POST':
        sprint.nome_sprint = request.form['nome_sprint']
        sprint.descricao = request.form['descricao']
        sprint.data_inicio = request.form['data_inicio']
        sprint.data_termino = request.form.get('data_termino')
        sprint.status = request.form['status']
        sprint.responsavel_id = request.form['responsavel_id']
        db.session.commit()
        return redirect(url_for('sprints.listar_sprints', projeto_id=sprint.projeto_id))
    usuarios = Usuario.query.all()
    return render_template('sprint_form.html', sprint=sprint, usuarios=usuarios)

@bp.route('/sprints/<int:sprint_id>/deletar/<int:projeto_id>')
def deletar_sprint(sprint_id, projeto_id):
    sprint = Sprint.query.get_or_404(sprint_id)
    db.session.delete(sprint)
    db.session.commit()
    return redirect(url_for('sprints.listar_sprints', projeto_id=projeto_id))
