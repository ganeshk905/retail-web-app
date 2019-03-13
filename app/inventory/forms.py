from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, DateField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Product


class InventoryForm(FlaskForm):
    """
    Form for users to create new account
    """
    id =  QuerySelectField(query_factory=lambda: Product.query.all(),
                                      get_label="id")
    product = StringField('Product Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    expiry_date = DateField('Expiry Date', format='%m/%d/%Y', validators=[DataRequired()])
    submit = SubmitField('Submit')

