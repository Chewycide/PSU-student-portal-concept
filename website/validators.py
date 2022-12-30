from website.models import Student
from wtforms.validators import ValidationError


# ---------- VALIDATORS ---------- #
def validate_password(form, field):
    """
        Validate password by using the psu_id input as a parameter to
        get the user from the database then checking the passwword of
        the user from the database if it matches the password input
        from the form.
        
        If the password does not match, raise an error
    """
    user = Student.query.filter_by(student_id_number=form.psu_id.data).first()
    if not user.student_password == field.data:
        raise ValidationError(message="Wrong Password")



# TODO: create a custom validator for user