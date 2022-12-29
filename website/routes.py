from website import app, login_manager, db
from flask import render_template, redirect, url_for, flash
from flask_login import logout_user, login_required, login_user
from website.forms import LoginForm, RegisterStudentForm
from website.models import Student


# ---------- USER CALLBACK ---------- #
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)


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
        # login_user()
        return redirect(url_for('login_page'))
    return render_template('login.html', login_form = login_form)


@app.route('/mainmenu')
@login_required
def main_menu():
    """Mainmenu route"""
    return render_template('main_menu.html')


@app.route('/enrollment')
@login_required
def enrollment():
    """Enrollment route"""
    return render_template('enrollment.html')


@app.route('/studentmaster')
@login_required
def student_master():
    """Student Master File Maintenance"""
    # TODO: render the data based on the user that logged in
    return render_template('student_master.html')


@app.route('/registeruser', methods=['POST', 'GET'])
def register():
    """Register user into the database. Used for testing for now"""
    registration_form = RegisterStudentForm()
    print(registration_form.errors)
    if registration_form.validate_on_submit():
        # create a new user object
        print(registration_form.validate_on_submit())
        new_user = Student(
            student_id_number=registration_form.student_id_number.data,
            student_fullname=registration_form.student_fullname.data,
            student_password=registration_form.student_password.data
        )


        db.session.add(new_user)
        db.session.commit()
        flash('Successfully registered')
        return redirect(url_for('login_page'))
    return render_template('register.html', registration_form=registration_form)
    # TODO: FIX VALIDATION