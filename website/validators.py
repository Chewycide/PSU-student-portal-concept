from website.models import Student
from wtforms.validators import ValidationError
from werkzeug.security import check_password_hash


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
    if user:
        if not check_password_hash(pwhash=user.student_password, password=field.data):
            raise ValidationError(message="Wrong password.")
    else:
        raise ValidationError()


def validate_user(form, field):
    """
        Check if user is not in the database then raise an error. This
        validator is expected to be in the PSU ID field.
    """
    user = Student.query.filter_by(student_id_number=form.psu_id.data).first()
    if not user:
        raise ValidationError(message="User does not exist. Please contact an Admin to register you to the database.")