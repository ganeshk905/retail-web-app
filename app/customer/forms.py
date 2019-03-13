from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField, IntegerField, SelectMultipleField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from datetime import datetime
from ..models import Product

class CustomerForm(FlaskForm):
    """
    Form for users to create new account
    """
    name = StringField('Product Name', validators=[DataRequired()])
    address = StringField("Address",  validators=[DataRequired()])
    mobile = IntegerField('Contact Number', validators=[DataRequired()])
    products = StringField("Products", validators=[DataRequired()])
    frequency = SelectMultipleField('Frequency',choices=[("Daily", "Daily"),("Alternate", "Alternate")])
    start_subsc_date = DateField('Subscription Date', default=datetime.now(), validators=[DataRequired()])
    is_active = SelectField("Is Active",choices=[("Subscription", "Subscription"),("Potential Customer", "Potential Customer")])
    submit = SubmitField('Submit')

