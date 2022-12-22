from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# ---------- APP INSTANCE ---------- #
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY']


# ---------- DATABASE MANAGER ---------- #
db = SQLAlchemy(app)

# ---------- LOGIN MANAGER ---------- #
login_manager = LoginManager(app)


# ---------- ROUTES IMPORT ---------- #
from website import routes