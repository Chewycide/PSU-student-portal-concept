from website import app, login_manager, db
from flask import render_template, redirect, url_for, flash
from flask_login import logout_user, login_required, login_user, current_user
from website.forms import LoginForm, RegisterStudentForm
from website.models import (
    Student,
    StudentPersonalInformation,
    StudentContactInformation,
    StudentEmergencyInformation,
    StudentOtherInformation
)
from werkzeug.security import generate_password_hash


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
        # Get user from the database
        user_queried = Student.query.filter_by(student_id_number=login_form.psu_id.data).first()
        if user_queried:
            login_user(user_queried)
            return redirect(url_for('main_menu'))

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
    """
        Student Master File Maintenance route

        These dictionaries gets the current user's data from the database and
        renders them to the website.
    """
    personal_info_dict = {
        "Student ID No.": current_user.student_id_number,
        "Surname" : current_user.student_personal_information[0].sur_name,
        "First Name" : current_user.student_personal_information[0].first_name,
        "Middle Name" : current_user.student_personal_information[0].middle_name,
        "Sex" : current_user.student_personal_information[0].sex,
        "Nationality" : current_user.student_personal_information[0].nationality,
        "Religion" : current_user.student_personal_information[0].religion,
        "Date of Birth" : current_user.student_personal_information[0].birth_date,
        "Place of Birth" : current_user.student_personal_information[0].birth_place,
        "Civil Status" : current_user.student_personal_information[0].civil_status,
        "Birth Order" : current_user.student_personal_information[0].birth_order,
        "LRN" : current_user.student_personal_information[0].learner_reference_num,
        "Mother Tongue" : current_user.student_personal_information[0].mother_tongue,
    }

    contact_info_dict = {
        "Postal Address" : current_user.student_contact_information[0].postal_address,
        "Home Phone No." : current_user.student_contact_information[0].home_phone_no,
        "Mobile Phone No." : current_user.student_contact_information[0].mobile_phone_no,
        "E-mail Address" : current_user.student_contact_information[0].email_address,
        "Residential Address" : current_user.student_contact_information[0].residential_address
    }

    emergency_info_dict = {
        "Contact Person" : current_user.student_emergency_information[0].contact_person,
        "Relationship" : current_user.student_emergency_information[0].cp_relationship,
        "Home Phone No." : current_user.student_emergency_information[0].home_phone_no,
        "Mobile Phone No." : current_user.student_emergency_information[0].mobile_phone_no
    }

    other_info_dict = {
        "Financial Source" : current_user.student_other_information[0].financial_source,
        "Date of Exam/Interview" : current_user.student_other_information[0].exam_interview_date
    }

    return render_template(
        'student_master.html',
        personal_info_dict=personal_info_dict,
        contact_info_dict=contact_info_dict,
        emergency_info_dict=emergency_info_dict,
        other_info_dict=other_info_dict
    )


@app.route('/registeruser', methods=['POST', 'GET'])
def register():
    """Register user into the database. Used for testing for now"""
    registration_form = RegisterStudentForm()
    if registration_form.validate_on_submit():
        hashed_password = generate_password_hash(
            password=registration_form.student_password.data,
            method="pbkdf2:sha256",
            salt_length=16
        )
        # create a new user object
        new_user = Student(
            student_id_number=registration_form.student_id_number.data,
            student_fullname=registration_form.student_fullname.data,
            student_password=hashed_password
        )
        db.session.add(new_user)

        # create Child objects
        user_personal_info = StudentPersonalInformation()
        user_personal_info.student = new_user

        user_contact_info = StudentContactInformation()
        user_contact_info.student = new_user

        user_emergency_info = StudentEmergencyInformation()
        user_emergency_info.student = new_user

        user_additional_info = StudentOtherInformation()
        user_additional_info.student = new_user

        db.session.add_all(
            [
                user_personal_info,
                user_contact_info,
                user_emergency_info,
                user_additional_info
            ]
        )
        db.session.commit()

        flash('Successfully registered')
        return redirect(url_for('login_page'))
    return render_template('register.html', registration_form=registration_form)


# TODO: add the ability of the user to edit their student's information at /studentmaster route