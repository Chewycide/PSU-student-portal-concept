from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """Form used on the login page"""
    
    psu_id = StringField('PSU ID', validators=[DataRequired(message='Insert your PSU ID'), Length(min=10, message='Invalid ID Length')])
    password = PasswordField('PASSWORD', validators=[DataRequired()])
    login = SubmitField('LOGIN')

    