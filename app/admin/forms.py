# Forms for admin blueprint
from ..constants import CONSTANTS
from flask_wtf import FlaskForm
from ..models import Department, Role
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField(CONSTANTS.NAME, validators=[DataRequired()])
    description = StringField(CONSTANTS.DESCRIPTION, validators=[DataRequired()])
    submit = SubmitField(CONSTANTS.SUBMIT)

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField(CONSTANTS.NAME, validators=[DataRequired()])
    description = StringField(CONSTANTS.DESCRIPTION, validators=[DataRequired()])
    submit = SubmitField(CONSTANTS.SUBMIT)

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label=CONSTANTS.NAME_LABEL)
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label=CONSTANTS.NAME_LABEL)
    submit = SubmitField(CONSTANTS.SUBMIT)