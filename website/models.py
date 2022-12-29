from website import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship


# ---------- DATABASE MODELS ---------- #
class Student(UserMixin, db.Model):
    """
        Student model for student login information

        This model has a one-to-many relationship with the following
        models:

        - StudentPersonalInformation
        - StudentContactInformation
        - StudentEmergencyInformation
        - StudentOtherInformation
    """
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)

    # model relationship objects
    student_personal_information = relationship("StudentPersonalInformation", back_populates="student")
    student_contact_information = relationship("StudentContactInformation", back_populates="student")
    student_emergency_information = relationship("StudentEmergencyInformation", back_populates="student")
    student_other_information = relationship("StudentOtherInformation", back_populates="student")

    # Columns
    student_id_number = db.Column(db.String, unique=True, nullable=False)
    student_fullname = db.Column(db.String, nullable=False)
    student_password = db.Column(db.String, nullable=False)


class StudentPersonalInformation(db.Model):
    """
        All of the student's personal information.

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_personal_info"
    id = db.Column(db.Integer, primary_key=True)

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_personal_information")

    # Personal information
    sur_name = db.Column(db.String)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    sex = db.Column(db.String(1))
    # NOTE: research about how to store images in database
    nationality = db.Column(db.String)
    religion = db.Column(db.String)
    birth_date = db.Column(db.String)
    birth_place = db.Column(db.String)
    civil_status = db.Column(db.String)
    birth_order = db.Column(db.String)
    learner_reference_num = db.Column(db.Integer)
    mother_tongue = db.Column(db.String)


class StudentContactInformation(db.Model):
    """
        All of the student's contact information.

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_contact_info"
    id = db.Column(db.Integer, primary_key=True)

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_contact_information")

    # Contact information
    postal_address = db.Column(db.String)
    home_phone_no = db.Column(db.Integer)
    mobile_phone_no = db.Column(db.Integer)
    email_address = db.Column(db.String)
    residential_address = db.Column(db.String)


class StudentEmergencyInformation(db.Model):
    """
        The student's contact in case of an emergency

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_emergency_info"
    id = db.Column(db.Integer, primary_key=True)

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_emergency_information")

    # Emergency Information
    contact_person = db.Column(db.String)
    # NOTE: cp is short for contact person
    cp_relationship = db.Column(db.String)
    home_phone_no = db.Column(db.Integer)
    mobile_phone_no = db.Column(db.Integer)


class StudentOtherInformation(db.Model):
    """
        Other information of the student
    """
    __tablename__ = "students_other_info"
    id = db.Column(db.Integer, primary_key=True)

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_other_information")

    # Other information
    financial_source = db.Column(db.String)
    exam_interview_date = db.Column(db.String)