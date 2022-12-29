from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """Form used on the login page"""
    psu_id = StringField('PSU ID:', validators=[DataRequired(message='Insert your PSU ID'), Length(min=10, message='Invalid ID Length')])
    password = PasswordField('PASSWORD:', validators=[DataRequired(), Length(min=7)])
    login = SubmitField('LOGIN')


class RegisterStudentForm(FlaskForm):
    """
        This form is used to register a student to the database.
        only login information is required to enter.
    """
    student_id_number = StringField('Student Id Number', validators=[DataRequired(), Length(min=10, message="Invalid Length")])
    student_fullname = StringField('Full Name', validators=[DataRequired()])
    student_password = PasswordField('Student Password', validators=[DataRequired(), Length(min=7)])
    confirm_student_password = PasswordField('Confirm Student Password', validators=[DataRequired(), EqualTo('student_password', message='Password does not match.')])
    register = SubmitField('REGISTER')
