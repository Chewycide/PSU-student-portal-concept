from website import app, login_manager
from flask import render_template, redirect, url_for
from flask_login import logout_user
from website.forms import LoginForm


# ---------- USER CALLBACK ---------- #
@login_manager.user_loader
def load_user(user_id):
    pass


# ---------- LOGOUT ---------- #
@app.route('/logout')
def logout():
    """Logout user from the portal and redirect to login page"""
    logout_user()
    return redirect(url_for('login_page'))


# ---------- ROUTES ---------- #

@app.route('/', methods=['POST', 'GET'])
def login_page():
    """Login route"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('login_page'))
    return render_template('login.html', login_form = login_form)


@app.route('/mainmenu')
def main_menu():
    """Mainmenu route"""
    return render_template('main_menu.html')


@app.route('/enrollment')
def enrollment():
    """Enrollment route"""
    return render_template('enrollment.html')

