from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import IntegerField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Product, SaleCategory

class SaleForm(FlaskForm):
    """
    Form for users to create new account
    """
    product_id = QuerySelectField('Product Id', query_factory=lambda: Product.query.all(),
                                      get_label="id")
    category = QuerySelectField('Sale category', query_factory=lambda: SaleCategory.query.all(),
                                      get_label="name", validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Submit')

