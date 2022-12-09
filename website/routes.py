from website import app
from flask import render_template, redirect, url_for
from website.forms import LoginForm


# ---------- APP INSTANCE ---------- #
@app.route('/', methods=['POST', 'GET'])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('login_page'))
    return render_template('login.html', login_form = login_form)


@app.route('/menu')
def main_menu():
    return render_template('main_menu.html')