from flask import Flask



# ---------- APP INSTANCE ---------- #
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY']


# ---------- ROUTES IMPORT ---------- #
from website import routes