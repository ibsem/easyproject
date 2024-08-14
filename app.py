from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/easyproject'
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from routes import projetos, sprints, usuarios

app.register_blueprint(projetos.bp)
app.register_blueprint(sprints.bp)
app.register_blueprint(usuarios.bp)

if __name__ == "__main__":
    app.run(debug=True)
