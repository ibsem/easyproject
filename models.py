from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    usuario_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    projetos = db.relationship('Projeto', backref='responsavel', lazy=True)
    sprints = db.relationship('Sprint', backref='responsavel', lazy=True)

class Projeto(db.Model):
    projeto_id = db.Column(db.Integer, primary_key=True)
    nome_projeto = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date, nullable=False)
    data_termino = db.Column(db.Date)
    usuario_responsavel_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'))
    sprints = db.relationship('Sprint', backref='projeto', lazy=True)

class Sprint(db.Model):
    sprint_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.projeto_id'))
    nome_sprint = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.Date, nullable=False)
    data_termino = db.Column(db.Date)
    status = db.Column(db.String(50))
    responsavel_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'))
