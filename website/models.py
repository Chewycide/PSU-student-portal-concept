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
    id = db.Column()

    # model relationship objects
    student_personal_information = relationship("StudentInformation", back_populates="student")
    student_contact_information = relationship("StudentInformation", back_populates="student")
    student_emergency_information = relationship("StudentInformation", back_populates="student")
    student_other_information = relationship("StudentInformation", back_populates="student")

    # Columns
    student_id_number = db.Column()
    student_fullname = db.Column()
    student_password = db.Column()


class StudentPersonalInformation(db.Model):
    """
        All of the student's personal information.

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_personal_info"
    id = db.Column()

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_personal_information")

    # Personal information
    sur_name = db.Column()
    first_name = db.Column()
    middle_name = db.Column()
    sex = db.Column()
    # NOTE: research about how to store images in database
    nationality = db.Column()
    religion = db.Column()
    birth_date = db.Column()
    birth_place = db.Column()
    civil_status = db.Column()
    birth_order = db.Column()
    learner_reference_num = db.Column()
    mother_tongue = db.Column()


class StudentContactInformation(db.Model):
    """
        All of the student's contact information.

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_contact_info"
    id = db.Column()

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_contact_information")

    # Contact information
    postal_address = db.Column()
    home_phone_no = db.Column()
    mobile_phone_no = db.Column()
    email_address = db.Column()
    residential_address = db.Column()


class StudentEmergencyInformation(db.Model):
    """
        The student's contact in case of an emergency

        This model has a one-to-one relationship with the
        'Student' model
    """
    __tablename__ = "students_emergency_info"
    id = db.Column()

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_emergency_information")

    # Emergency Information
    contact_person = db.Column()
    # NOTE: cp is short for contact person
    cp_relationship = db.Column()
    home_phone_no = db.Column()
    mobile_phone_no = db.Column()


class StudentOtherInformation(db.Model):
    """
        Other information of the student
    """
    __tablename__ = "students_other_info"
    id = db.Column()

    # parent_student_id is the primary key of the 'Student' model
    parent_student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    # relationship object
    student = relationship("Student", back_populates="student_other_information")

    # Other information
    financial_source = db.Column()
    exam_interview_date = db.Column()