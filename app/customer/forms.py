from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from ..models import Product, DeliveryFrequency

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SelectField, StringField, IntegerField, SubmitField

class CustomerForm(FlaskForm):
    """
    Form for users to create new account
    """
    status_list = [(True, "Yes"),(False, "No")]
    name = StringField('Name', validators=[DataRequired()])
    address = StringField("Address",  validators=[DataRequired()])
    mobile = IntegerField('Contact Number', validators=[DataRequired()])
    products = QuerySelectField("Products", query_factory=lambda: Product.query.all(),
                                  get_label="name", validators=[DataRequired()])
    frequency = QuerySelectField('Frequency',query_factory=lambda: DeliveryFrequency.query.all(),
                                  get_label="name", validators=[DataRequired()])
    start_subsc_date = DateField('Subscription Date',format='%Y-%m-%d', validators=[DataRequired()])
    is_active = SelectField("Is Active",coerce=bool, choices=status_list, validators=[DataRequired()])
    submit = SubmitField('Submit')

