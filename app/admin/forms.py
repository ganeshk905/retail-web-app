# Forms for admin blueprint
from flask_wtf import FlaskForm
from ..models import Department, Role
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField("Department", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="id")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="id")
    submit = SubmitField("Submit")
