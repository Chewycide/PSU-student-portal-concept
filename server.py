from flask import Flask, render_template, url_for, redirect, request
from forms import LoginForm


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['SECRET_KEY']


# -------------------------- ROUTES
@app.route('/', methods=['POST', 'GET'])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('login_page'))
    return render_template('login.html', login_form = login_form)


if __name__ == '__main__':
    app.run(debug=True)